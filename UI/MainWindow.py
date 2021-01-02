#
# 主窗口
#

import os

import backtrader
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DetailsWindow import DetailsWindow
from InstructionWindow import InstructionWindow
from ResultWindow import ResultWindow
from DownloadWindow import DownloadWindow
from StrategyDescriptionWindow import StrategyDescriptionWindow
from MyStrategy import BackTesting,FormatCsv
from ui_MainCentralWidget import Ui_MainCentralWidget

# 已有股票数据更新子线程
class updateCsvThread(QThread):
    # 自定义Signal
    update_end = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        # 股票数据更新
        FormatCsv.updatecsv()
        self.update_end.emit()
        pass

# 回测线程
class backtraderThread(QThread):
    # 自定义Signal
    backtrader_end = Signal(dict,list,backtrader.cerebro.Cerebro,str,str)
    showError = Signal(str)
    def __init__(self):
        super().__init__()

    # 设置参数
    def setup(self,code,fromdate,todate,strategyname,cash,commission):
        self.code = code
        self.fromdate = fromdate
        self.todate = todate
        self.strategyname = strategyname
        self.cash = cash
        self.commission = commission
    def run(self):
        try:
            # 生成回测数据以便读取使用
            FormatCsv.incsv(code=self.code, fromdate=self.fromdate, todate=self.todate)
            # 回测函数
            params, strategyresult, cerebro = BackTesting.start(
                datapath="./MyStrategy/datas/datachoice.csv",
                Strategy=self.strategyname, code=self.code, setcash=self.cash,
                comm=self.commission)
            # 触发信号，发射参数
            self.backtrader_end.emit(params, strategyresult, cerebro,self.strategyname, self.code)
        except KeyError:
            self.showError.emit("KeyError")
        except ValueError:
            self.showError.emit("ValueError")
        except IndexError:
            self.showError.emit("IndexError")
        pass

# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #MainWindow初始化
        self.newWindows = []
        self.setWindowTitle("股票回测")
        self.setGeometry(400,100,1150,850)
        self.setMinimumSize(1150,850)
        #设置MainWindow的CentralWidget的UI
        self.ui = Ui_MainCentralWidget()
        central = QWidget()
        self.ui.setupUi(central)
        self.setCentralWidget(central)
        #菜单栏设置
        menubar = QMenuBar()
        self.setMenuBar(menubar)

        # 各菜单功能设置
        menu1 = menubar.addMenu("文件(&F)")
        self.close_action = menu1.addAction("退出(&Q)")

        menu2 = menubar.addMenu("下载(&D)")
        self.download_action = menu2.addAction("数据下载(&D)")
        self.download_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_D))

        self.update_action = menu2.addAction("数据更新(&U)")
        self.update_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_U))

        menu3 = QMenu('帮助(&H)')
        menubar.addMenu(menu3)
        self.instruction_action = QAction('使用说明(&H)')
        self.instruction_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_Question))
        menu3.addAction(self.instruction_action)
        menu3.addSeparator()
        self.strategydescription_action = menu3.addAction("策略说明")

        #回测线程
        self.backtraderThread = backtraderThread()
        self.backtraderThread.backtrader_end.connect(self.showResult)
        self.backtraderThread.showError.connect(self.showError)

        #更新数据线程
        self.updateCsvThread = updateCsvThread()
        self.updateCsvThread.update_end.connect(self.updateEnd)

        #连接Signal与Slot
        self.ui.button.clicked.connect(self.handleCalc)
        self.instruction_action.triggered.connect(self.openInstructionWindow)
        self.download_action.triggered.connect(self.openDownloadWindow)
        self.update_action.triggered.connect(self.updateCsv)
        self.close_action.triggered.connect(self.close)
        self.strategydescription_action.triggered.connect(self.openStrategyDescriptionWindow)

        #Tab设置
        QWidget.setTabOrder(self.ui.dataline,self.ui.strategyline)
        QWidget.setTabOrder(self.ui.strategyline, self.ui.cashline)
        QWidget.setTabOrder(self.ui.cashline, self.ui.commline)

    def handleCalc(self):

        #策略名
        strategyname = self.ui.strategyline.text()

        #初始资金
        cash = self.ui.cashline.text()
        if cash :
            cash = float(cash)
        else:
            cash = 100

        #手续费
        commission = self.ui.commline.text()
        if commission:
            commission = float(commission)
        else:
            commission = 0.003

        # 数据csv文件
        fromdate = self.ui.datebegin.ui.line.text()
        todate = self.ui.dateend.ui.line.text()
        code = self.ui.dataline.text()[0:6]
        datapath = './MyStrategy/datas/' + code + '.csv'

        # 判断是否存在该股票数据
        if os.path.exists(datapath):
            # 回测线程参数设置
            self.backtraderThread.setup(code,fromdate,todate,strategyname,cash,commission)
            # 回测过程中禁止再次回测
            if not self.backtraderThread.isRunning():
                # 状态栏显示
                self.statusBar().showMessage('正在回测...')
                self.statusBar().show()
                # 线程开始
                self.backtraderThread.start()
        else:
            QMessageBox.critical(
                self,
                '错误',
                '本地不存在此股票数据！'
            )

    # 展示回测结果
    def showResult(self,params, strategyresult, cerebro, Strategyname, code):
        # 关闭状态栏
        self.statusBar().close()
        # 回测时，策略使用多组参数
        if strategyresult.__len__() > 1:
            self.openResultWindow(params, strategyresult, cerebro, Strategyname, code)
        # 回测时，策略使用一组参数
        elif strategyresult.__len__() == 1:
            # 回测过后的，策略实体
            strategy = strategyresult[0][1]
            # 生成回测结果图
            fig = cerebro.plotone(strategy, style='bar')
            fig[0].suptitle(Strategyname + code)
            # 回测日志
            log = strategy.buysellLog \
                  + "总收益率:%.2f%%\n"%(strategy.analyzers.returns.get_analysis()['rtot']*100)\
                  + "日平均收益率:%.4f%%\n"%(strategy.analyzers.returns.get_analysis()['ravg']*100)\
                  + "年平均收益率:%.2f%%"%(strategy.analyzers.returns.get_analysis()['rnorm']*100)
            # 结果详情窗口实例化
            detailsWindow = DetailsWindow(fig[0],log)
            self.newWindows.append(detailsWindow)
            self.newWindows[-1].show()

    # 回测线程的异常处理函数
    def showError(self,Error):
        self.statusBar().close()
        if Error=="KeyError":
            QMessageBox.critical(
                self,
                '错误',
                '本地不存在此策略！'
            )
        elif Error=="ValueError":
            QMessageBox.critical(
                self,
                '错误',
                '输入正确的日期格式！'
            )
        elif Error=="IndexError":
            QMessageBox.critical(
                self,
                '错误',
                '回测日期过短！'
            )

    # 打开使用多组参数回测的结果窗口
    def openResultWindow(self,params,strategyresult,cerebro,Strategyname,code):
        resultWindow = ResultWindow()
        resultWindow.setFigure(params,strategyresult,cerebro,Strategyname,code)
        self.newWindows.append(resultWindow)
        self.newWindows[-1].show()

    # 打开说明窗口
    def openInstructionWindow(self):
        self.instructuonWindow = InstructionWindow()
        self.instructuonWindow.show()

    # 打开下载窗口
    def openDownloadWindow(self):
        self.downloadWindow = DownloadWindow()
        self.downloadWindow.show()
        self.downloadWindow.ui.pushButton.clicked.connect(self.download)

    # 打开策略说明窗口
    def openStrategyDescriptionWindow(self):
        strategyList = list(BackTesting._STRATS.keys())
        self.strategyDescriptionWindow =StrategyDescriptionWindow(strategyList)
        self.strategyDescriptionWindow.show()

    # 更新已有股票数据
    def updateCsv(self):
        self.statusBar().showMessage('正在更新...')
        self.statusBar().show()
        if not self.updateCsvThread.isRunning():
            self.updateCsvThread.start()

    # 股票数据更新结束，调用
    def updateEnd(self):
        QMessageBox.information(
            self,
            '数据更新',
            '更新成功！'
        )
        self.statusBar().close()
        self.updateCsvThread.terminate()

    # 下载股票数据
    def download(self):
        code = self.downloadWindow.ui.inputLine.text()
        filename = './MyStrategy/datas/' + code + '.csv'
        if os.path.exists(filename):
            QMessageBox.information(
                self.downloadWindow,
                '股票已存在',
                '该股票代码已存在，无需下载！'
            )
        else:
            result = FormatCsv.downloadcsv(code)
            if not result:
                QMessageBox.critical(
                    self.downloadWindow,
                    '错误',
                    '该股票代码输入错误或不存在！'
                )
            else:
                QMessageBox.information(
                    self.downloadWindow,
                    '下载成功',
                    '下载成功！'
                )
            # 刷新主窗口中的股票代码列表
            dataList = []
            with open('./MyStrategy/datas/codelist.csv', "r", encoding="gbk") as f:
                text = f.readlines()
            for data in text:
                code = data.rstrip()
                dataList.append(code)
            self.ui.datamodel.setStringList(dataList)