#
# 策略说明窗口
#
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *
class StrategyDescriptionWindow(QWidget):
    def __init__(self,strategyList):
        super().__init__()
        self.setGeometry(100,100,1500,800)
        self.setWindowTitle("策略说明")
        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        self.setLayout(layout)
        self.treewidget = QTreeWidget(self)
        self.treewidget.setMaximumWidth(200)
        self.treewidget.headerItem().setText(0,"策略")
        for strategy in strategyList:
            qtreewidgetitem = QTreeWidgetItem(self.treewidget)
            qtreewidgetitem.setText(0,strategy)
        layout.addWidget(self.treewidget)

        self.tabwidget = QTabWidget()
        self.tabwidget.setTabsClosable(True)
        self.tabwidget.setMovable(True)
        self.tabwidget.setStyleSheet(u"background-color: rgb(160, 160, 160);")

        layout.addWidget(self.tabwidget)

        self.treewidget.itemDoubleClicked.connect(self.opentab)
        self.tabwidget.tabCloseRequested.connect(self.closetab)

    def opentab(self,item):
        self.tabwidget.setStyleSheet("")
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        p = QPlainTextEdit()
        font = QFont()
        font.setFamily(u"黑体")
        font.setPointSize(10)
        p.setFont(font)
        layout.addWidget(p)
        with open("./Mystrategy/strategys_description/"+item.text(0)+'.txt','r',encoding='utf-8') as f:
            text = f.read()
        p.setPlainText(text)
        p.setReadOnly(True)
        index = self.tabwidget.addTab(widget, item.text(0))
        self.tabwidget.setCurrentIndex(index)


    def closetab(self,index):

        self.tabwidget.widget(index).close()
        self.tabwidget.removeTab(index)
        if self.tabwidget.count() == 0:
            self.tabwidget.setStyleSheet(u"background-color: rgb(160, 160, 160);")