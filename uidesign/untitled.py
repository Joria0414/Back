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


class Ui_DetailsWindow(object):
    def setupUi(self, DetailsWindow):
        if not DetailsWindow.objectName():
            DetailsWindow.setObjectName(u"DetailsWindow")
        DetailsWindow.resize(1127, 728)
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(12)
        DetailsWindow.setFont(font)
        DetailsWindow.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(DetailsWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 20)
        self.treeWidget = QTreeWidget(DetailsWindow)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.header().setVisible(True)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.tabWidget = QTabWidget(DetailsWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(160, 160, 160);")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(DetailsWindow)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(DetailsWindow)
    # setupUi

    def retranslateUi(self, DetailsWindow):
        DetailsWindow.setWindowTitle("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DetailsWindow", u"1", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DetailsWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("DetailsWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("DetailsWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

