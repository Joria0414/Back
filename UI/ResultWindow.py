#
# 回测时，若策略使用多组参数，打开此窗口
#

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from pylab import *

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from DetailsWindow import DetailsWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt


class ResultWindow(QWidget):
    def __init__(self, parent=None):
        # 父类初始化方法
        super(ResultWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('回测结果')
        self.setGeometry(300,200,1200,700)

        # 布局
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 10, 20, 50)
        self.figure = plt.figure()
        # 画布控件设置
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    # 画图，
    # 参数：params(dict)：策略参数字典，strategyResult(list)：[收益率，回测策略]列表，
    #       cerebro(backtrader.Cerebro):回测实体，strategyName,code(str)：回测策略名，回测股票代码
    def setFigure(self,params,strategyResult,cerebro,strategyName,code):
        self.strategyName = strategyName
        self.code = code
        self.strategyResult = strategyResult
        self.cerebro = cerebro
        # 获取回测结果中，每个策略的收益率百分比
        data = [100 * p[0] for p in self.strategyResult]
        # 根据参数个数画图
        if params.__len__() == 2:
            param = [param for param in params]
            _x = params[param[0]]
            _y = params[param[1]]
            self.xlen = _x.__len__()
            self.ylen = _y.__len__()
            #存储画图信息[参数内容(str)，颜色(list)，收益率(list)]
            plobar = []
            i = 0
            for x in _x:
                for y in _y:
                    if(data[i])>0:
                        color = [1,0,0]
                    else:
                        color = [0,1,0]
                    plobar.append(["参数一："+str(x)+"，参数二："+str(y),color,data[i]])
                    i += 1
            # 根据收益率排序
            plobar.sort(key=lambda x:x[2])

            width = [abs(i[2]) for i in plobar]
            color = [i[1] for i in plobar]
            tick_label = [i[0] for i in plobar]
            ax1 = self.figure.add_axes([0.4, 0.1, 0.4, 0.9])
            # y轴坐标，横向柱状图x方向宽度，颜色，坐标标签
            ax1.barh(range(len(data)),width=width,color=color,tick_label=tick_label)

            #其他控件
            submitLayout = QHBoxLayout()
            label_1 = QLabel("参数一：")
            label_1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.combobox_1 = QComboBox(self)
            self.combobox_1.addItems([str(item) for item in _x])

            label_2 = QLabel("参数二：")
            label_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.combobox_2 = QComboBox(self)
            self.combobox_2.addItems([str(item) for item in _y])

            submitbutton = QPushButton("查看")
            # 点击按钮，打开回测结果详情窗口
            submitbutton.clicked.connect(self.openDetailsWindow)

            submitLayout.addWidget(label_1)
            submitLayout.addWidget(self.combobox_1)
            submitLayout.addWidget(label_2)
            submitLayout.addWidget(self.combobox_2)
            submitLayout.addWidget(submitbutton)
            self.layout.addLayout(submitLayout)



            # 三维柱状图
            # data = np.array([p[0] for p in strategyResult])*100
            # if params.__len__()==2:
            #     param = [param for param in params]
            #     _x = np.array(params[param[1]])
            #     _y = np.array(params[param[0]])
            #
            # _xx, _yy = np.meshgrid(_x, _y)
            # x, y = _xx.ravel(), _yy.ravel()
            # self.figure = plt.figure()
            # axes1 = self.figure.add_subplot(111,projection='3d')
            # axes1.set_xlabel(param[1])
            # axes1.set_ylabel(param[0])
            # axes1.set_zlabel('年收益率(%)')
            # colorlist = []
            # for i in data:
            #     if i>0:
            #         colorlist.append([1,0,0])
            #     else:
            #         colorlist.append([0,1,0])
            # color =np.array(colorlist)
            # axes1.bar3d(x,y,np.zeros_like(data),0.5,0.5,data,color,shade=True)
        plt.xlabel("收益率百分比（%）")
        # plt.legend()

    newWindows = []
    def openDetailsWindow(self):
        # 通过下拉菜单选择，获得所选策略所处下标
        param_1_Index = self.combobox_1.currentIndex()
        param_2_Index = self.combobox_2.currentIndex()
        strategyIndex = param_1_Index * self.ylen + param_2_Index
        # 通过下标获得策略实体
        strategy = self.strategyResult[strategyIndex][1]
        # 生成策略结果图
        fig = self.cerebro.plotone(strategy,style='bar')
        fig[0].suptitle(self.strategyName+self.code)
        # 获取策略交易日志
        log = strategy.buysellLog \
              + "总收益率:%.2f%%\n" % (strategy.analyzers.returns.get_analysis()['rtot'] * 100) \
              + "日平均收益率:%.4f%%\n" % (strategy.analyzers.returns.get_analysis()['ravg'] * 100) \
              + "年平均收益率:%.2f%%" % (strategy.analyzers.returns.get_analysis()['rnorm'] * 100)
        # 回测结果详情窗口实例化
        detailsWindow = DetailsWindow(fig[0],log)
        self.newWindows.append(detailsWindow)
        self.newWindows[-1].show()
