#
# 帮助说明窗口
#

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import InstructionImages_rc


# ui
class Ui_InstructionWindow(object):
    def setupUi(self, InstructionWindow):
        if not InstructionWindow.objectName():
            InstructionWindow.setObjectName(u"InstructionWindow")
        InstructionWindow.setGeometry(400,100,1100,800)
        InstructionWindow.setMaximumSize(1100,800)
        #字体设置
        font = QFont()
        font.setFamily(u"黑体")
        font.setPointSize(15)
        InstructionWindow.setFont(font)
        #说明内容
        self.page = 0
        self.maxPage = 5
        self.minPage = 0
        self.instruction = []
        self.instruction.append("1、输入股票代码(若本地无此股票，需下载，点击菜单栏的下载->数据下载)")
        self.instruction.append("2、输入股票代码，下载股票数据")
        self.instruction.append("3、输入策略、初始资金、手续费百分比和回测时间")
        self.instruction.append("4、回测使用策略为多参数时，产生柱状图（比较各参数下的收益率）；选择参数，点击查看，展示该参数下的回归测试详情")
        self.instruction.append("5、回归测试详情")
        self.instruction.append("6、回归测试结果图说明")

        #布局设置
        self.gridLayout = QGridLayout(InstructionWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(-1, -1, -1, 1)
        self.pushButton_2 = QPushButton(InstructionWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.label = QLabel(InstructionWindow)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton = QPushButton(InstructionWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.hide()
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.graphicsView = QGraphicsView(InstructionWindow)
        self.graphicsView.setObjectName(u"graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 2)

        #说明图片
        self.image = []
        self.image.append(u"border-image:url(:/Instruction_1.jpg)")
        self.image.append(u"border-image:url(:/Instruction_2.jpg)")
        self.image.append(u"border-image:url(:/Instruction_3.jpg)")
        self.image.append(u"border-image:url(:/Instruction_4.jpg)")
        self.image.append(u"border-image:url(:/Instruction_5.jpg)")
        self.image.append(u"border-image:url(:/Instruction_6.jpg)")
        self.graphicsView.setStyleSheet(self.image[0])
        #控件内容设置
        self.retranslateUi(InstructionWindow)
        #连接Signal与Slot
        self.pushButton_2.setShortcut(QKeySequence(Qt.Key_Right))
        self.pushButton.setShortcut(QKeySequence(Qt.Key_Left))
        self.pushButton_2.clicked.connect(self.nextPage)
        self.pushButton.clicked.connect(self.previousPage)

        QMetaObject.connectSlotsByName(InstructionWindow)
    # setupUi

    def retranslateUi(self, InstructionWindow):
        InstructionWindow.setWindowTitle(QCoreApplication.translate("InstructionWindow", u"使用说明", None))
        self.label.setText(QCoreApplication.translate("InstructionWindow", self.instruction[0], None))
        self.pushButton_2.setText(QCoreApplication.translate("InstructionWindow", u"\u4e0b\u4e00\u9875", None))
        self.pushButton.setText(QCoreApplication.translate("InstructionWindow", u"\u4e0a\u4e00\u9875", None))
    # retranslateUi

    # 上下页Slot
    def nextPage(self):
        self.pushButton.show()
        self.page += 1
        if (self.page==self.maxPage):
            self.pushButton_2.hide()
        self.graphicsView.setStyleSheet(self.image[self.page])
        self.label.setText(self.instruction[self.page])
    def previousPage(self):
        self.pushButton_2.show()
        self.page -= 1
        if (self.page==self.minPage):
            self.pushButton.hide()
        self.graphicsView.setStyleSheet(self.image[self.page])
        self.label.setText(self.instruction[self.page])

# 自定义控件类
class InstructionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InstructionWindow()
        self.ui.setupUi(self)

