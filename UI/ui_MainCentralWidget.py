#
# 主窗口中心窗口UI
#

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DateTable import DateTable


class Ui_MainCentralWidget(object):
    def setupUi(self, MainCentralWidget):
        #股票代码列表
        self.dataList = []
        # 读取已有数据的股票代码
        with open('./MyStrategy/datas/codelist.csv', "r", encoding="gbk") as f:
            dataList = f.readlines()
        for data in dataList:
            code = data.rstrip()
            self.dataList.append(code)

        #策略列表
        self.strategyList = []
        # 读取已有策略的策略名
        with open('./MyStrategy/datas/StrategyList.csv', "r", encoding="gbk") as f:
            strategyList = f.readlines()
        for strategy in strategyList:
            strategyName = strategy.split(",")[0]
            self.strategyList.append(strategyName)


        if not MainCentralWidget.objectName():
            MainCentralWidget.setObjectName(u"MainCentralWidget")
        # 字体设置
        font = QFont()
        font.setFamily(u"黑体")
        font.setPointSize(10)
        MainCentralWidget.setFont(font)

        # 主布局
        self.verticalLayout = QVBoxLayout(MainCentralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # 树控件（暂时无用）
        self.treeWidget = QTreeWidget(MainCentralWidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1.setCheckState(0, Qt.Unchecked);
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3.setCheckState(0, Qt.Unchecked);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem4.setCheckState(0, Qt.Unchecked);
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)

        self.verticalLayout.addWidget(self.treeWidget)

        # 输入信息布局（分布局）
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        # 手续费单行文本控件及其标签控件
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(MainCentralWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 30))
        self.label_6.setMaximumSize(QSize(80, 30))

        self.commline = QLineEdit(MainCentralWidget)
        self.commline.setObjectName(u"commline")
        self.commline.setMaximumSize(QSize(240, 25))
        self.commline.setMinimumSize(QSize(240, 25))

        self.horizontalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_6.addWidget(self.commline)

        # 加入信息布局
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)

        # 截止日期日历控件及其标签控件
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(MainCentralWidget)
        self.label_5.setAlignment(Qt.AlignTop)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 170))
        self.label_5.setMaximumSize(QSize(80, 170))

        self.dateend = DateTable(MainCentralWidget)
        self.dateend.setObjectName(u"dateend")
        self.dateend.setMaximumSize(QSize(240, 175))
        self.dateend.setMinimumSize(QSize(240, 175))

        self.horizontalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_3.addWidget(self.dateend)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        # 开始日期日历控件及其标签控件
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(MainCentralWidget)
        self.label_4.setAlignment(Qt.AlignTop)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 170))
        self.label_4.setMaximumSize(QSize(80, 170))

        self.datebegin = DateTable(MainCentralWidget)
        self.datebegin.setObjectName(u"datebegin")
        self.datebegin.setMaximumSize(QSize(240,175 ))
        self.datebegin.setMinimumSize(QSize(240,175))

        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.addWidget(self.datebegin)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        # 策略单行文本控件及其标签控件
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(MainCentralWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 30))
        self.label_2.setMaximumSize(QSize(80, 30))

        self.strategyline = QLineEdit(MainCentralWidget)
        self.strategyline.setObjectName(u"strategyline")
        # 模糊搜索
        model = QStringListModel()
        model.setStringList(self.strategyList)
        self.strategyFilterModel = QSortFilterProxyModel()
        self.strategyFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.strategyFilterModel.setSourceModel(model)
        completer = QCompleter(self.strategyFilterModel)
        completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        completer.setMaxVisibleItems(6)
        # 搜索过滤
        self.strategyline.textEdited.connect(self.strategyFilterModel.setFilterFixedString)
        self.strategyline.setCompleter(completer)
        self.strategyline.setMaximumSize(QSize(240,  25))
        self.strategyline.setMinimumSize(QSize(240,  25))

        self.horizontalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_5.addWidget(self.strategyline)

        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

        # 资金单行文本控件及其标签控件
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(MainCentralWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 30))
        self.label_3.setMaximumSize(QSize(80, 30))

        self.cashline = QLineEdit(MainCentralWidget)
        self.cashline.setObjectName(u"cashline")
        self.cashline.setMaximumSize(QSize(240, 25))
        self.cashline.setMinimumSize(QSize(240, 25))

        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_4.addWidget(self.cashline)

        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        # 股票代码单行文本控件及其标签控件
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(MainCentralWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 30))
        self.label.setMaximumSize(QSize(80, 30))

        #股票搜索
        self.dataline = QLineEdit(MainCentralWidget)
        self.dataline.setObjectName(u"dataline")
        #模糊搜索
        self.datamodel = QStringListModel()
        self.datamodel.setStringList(self.dataList)
        self.dataFilterModel = QSortFilterProxyModel()
        self.dataFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.dataFilterModel.setSourceModel(self.datamodel)
        completer = QCompleter(self.dataFilterModel)
        completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        completer.setMaxVisibleItems(6)
        self.dataline.textEdited.connect(self.dataFilterModel.setFilterFixedString)
        self.dataline.setCompleter(completer)
        self.dataline.setMinimumSize(QSize(240, 25))
        self.dataline.setMaximumSize(QSize(240, 25))

        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.dataline)

        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        # 提交按钮控件
        self.button = QPushButton(MainCentralWidget)
        self.button.setObjectName(u"button")
        self.button.setFocusPolicy(Qt.ClickFocus)
        self.button.setMaximumSize(QSize(240, 30))
        self.button.setMinimumSize(QSize(240, 30))

        self.gridLayout_3.addWidget(self.button,3,1,1,1)

        # 信息布局加入主布局
        self.verticalLayout.addLayout(self.gridLayout_3)

        # 控件文本内容初始化
        self.retranslateUi(MainCentralWidget)

        # Signal与Slot连接
        self.dataline.returnPressed.connect(self.strategyline.setFocus)
        self.strategyline.returnPressed.connect(self.cashline.setFocus)
        self.cashline.returnPressed.connect(self.commline.setFocus)

        QMetaObject.connectSlotsByName(MainCentralWidget)
    # setupUi

    # 控件文本内容初始化
    def retranslateUi(self, MainCentralWidget):
        MainCentralWidget.setWindowTitle(QCoreApplication.translate("MainCentralWidget", u"\u80a1\u7968\u56de\u6d4b", None))
#if QT_CONFIG(whatsthis)
        MainCentralWidget.setWhatsThis(QCoreApplication.translate("MainCentralWidget", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u7b56\u7565", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainCentralWidget", u"2", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u5b50\u9879\u76ee", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainCentralWidget", u"1", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u5b50\u9879\u76ee", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem7.child(2)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem7.child(3)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainCentralWidget", u"\u65b0\u5efa\u9879\u76ee", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.button.setText(QCoreApplication.translate("MainCentralWidget", u"\u63d0\u4ea4", None))
        self.label_6.setText(QCoreApplication.translate("MainCentralWidget", u"\u624b\u7eed\u8d39\uff1a", None))
        self.commline.setPlaceholderText(QCoreApplication.translate("MainCentralWidget", u"\u8f93\u5165\u624b\u7eed\u8d39\u767e\u5206\u6bd4", None))
        self.label_5.setText(QCoreApplication.translate("MainCentralWidget", u"\u7ed3\u675f\u65e5\u671f\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainCentralWidget", u"\u5f00\u59cb\u65e5\u671f\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainCentralWidget", u"\u7b56\u7565\uff1a", None))

        self.label_3.setText(QCoreApplication.translate("MainCentralWidget", u"\u521d\u59cb\u8d44\u91d1\uff1a", None))
        self.cashline.setPlaceholderText(QCoreApplication.translate("MainCentralWidget", u"\u8f93\u5165\u521d\u59cb\u8d44\u91d1", None))
        self.label.setText(QCoreApplication.translate("MainCentralWidget", u"\u80a1\u7968\u4ee3\u7801\uff1a", None))

    # retranslateUi

