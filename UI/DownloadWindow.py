#
# 下载股票数据窗口
#

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DownloadWindow(object):
    def setupUi(self, DownloadWindow):
        if not DownloadWindow.objectName():
            DownloadWindow.setObjectName(u"DownloadWindow")
        DownloadWindow.resize(262, 301)
        DownloadWindow.setMinimumSize(QSize(262, 301))
        DownloadWindow.setMaximumSize(QSize(262, 301))
        self.inputLine = QLineEdit(DownloadWindow)
        self.inputLine.setObjectName(u"inputLine")
        self.inputLine.setGeometry(QRect(40, 100, 181, 41))
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(15)
        self.inputLine.setFont(font)
        self.pushButton = QPushButton(DownloadWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 170, 121, 31))
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(14)
        self.pushButton.setFont(font1)

        self.retranslateUi(DownloadWindow)
        self.inputLine.returnPressed.connect(self.pushButton.click)

        QMetaObject.connectSlotsByName(DownloadWindow)
    # setupUi

    def retranslateUi(self, DownloadWindow):
        DownloadWindow.setWindowTitle(QCoreApplication.translate("DownloadWindow", u"\u4e0b\u8f7d\u80a1\u7968\u6570\u636e", None))
        self.inputLine.setPlaceholderText(QCoreApplication.translate("DownloadWindow", u"\u8f93\u5165\u80a1\u7968\u4ee3\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("DownloadWindow", u"\u63d0\u4ea4", None))
    # retranslateUi

class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DownloadWindow()
        self.ui.setupUi(self)