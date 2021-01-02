# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import image1_rc

class Ui_InstructionWindow(object):
    def setupUi(self, InstructionWindow):
        if not InstructionWindow.objectName():
            InstructionWindow.setObjectName(u"InstructionWindow")
        InstructionWindow.resize(1127, 728)
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(9)
        InstructionWindow.setFont(font)
        self.gridLayout = QGridLayout(InstructionWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(InstructionWindow)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"")

        self.gridLayout.addWidget(self.graphicsView, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(InstructionWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, -1)
        self.label_2 = QLabel(InstructionWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton = QPushButton(InstructionWindow)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(InstructionWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_2.setBaseSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.label = QLabel(InstructionWindow)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(InstructionWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(InstructionWindow)
    # setupUi

    def retranslateUi(self, InstructionWindow):
        InstructionWindow.setWindowTitle("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("InstructionWindow", u"6000000000000", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("InstructionWindow", u"\u9875", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("InstructionWindow", u"\u9875", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("InstructionWindow", u"\u9875", None))
        self.label_2.setText(QCoreApplication.translate("InstructionWindow", u"\u8270\u82e6\u6492\u65e6\u53d1\u4f60\u770b\u662f\u5426\u80fd", None))
        self.pushButton.setText(QCoreApplication.translate("InstructionWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("InstructionWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("InstructionWindow", u"1\u3001\u8f93\u5165\u80a1\u7968\u4ee3\u7801(\u82e5\u672c\u5730\u65e0\u6b64\u80a1\u7968\uff0c\u9700\u4e0b\u8f7d\uff0c\u4e0b\u8f7d\u65b9\u5f0f\u5728\u4e0b\u4e00\u9875)", None))
    # retranslateUi

