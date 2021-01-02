#
# 自定义日历空间
#
from PySide2.QtCore import *
from PySide2.QtWidgets import *

# 自定义单行文本
class MyLine(QLineEdit):
    # 自定义Signal
    infocus = Signal()
    outfocus = Signal()
    def focusOutEvent(self, QFocusEvent):
        if QFocusEvent.lostFocus()==True:
            # Signal发射
            self.outfocus.emit()
    def focusInEvent(self, QFocusEvent):
        if QFocusEvent.gotFocus()==True:
            self.clear()
            self.infocus.emit()

# 日历空间类
class DateTable(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.ui = Ui_DateTable()
        self.resize(240,170)
        # 初始化界面
        self.ui.setupUi(self)


# 日历UI
class Ui_DateTable(object):
    def setupUi(self, DataTable):
        if not DataTable.objectName():
            DataTable.setObjectName(u"DataTable")
        # 日历文本框设置
        self.line = MyLine(DataTable)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(240, 25))
        self.line.setMaximumSize(QSize(240, 25))
        self.line.setFocusPolicy(Qt.ClickFocus)

        # 日历年月日设置
        self.table1 = QTableWidget(DataTable)
        if (self.table1.columnCount() < 4):
            self.table1.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table1.rowCount() < 5):
            self.table1.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table1.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table1.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table1.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table1.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table1.setItem(1, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table1.setItem(1, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table1.setItem(1, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table1.setItem(1, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table1.setItem(2, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table1.setItem(2, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table1.setItem(2, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table1.setItem(2, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table1.setItem(3, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table1.setItem(3, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table1.setItem(3, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table1.setItem(3, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table1.setItem(4, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table1.setItem(4, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table1.setItem(4, 2, __qtablewidgetitem27)
        self.table1.setObjectName(u"table1")
        self.table1.setEnabled(True)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table1.sizePolicy().hasHeightForWidth())
        self.table1.setSizePolicy(sizePolicy)
        self.table1.setMinimumSize(QSize(240, 150))
        self.table1.setMaximumSize(QSize(240, 150))
        self.table1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table1.setAutoScroll(False)
        self.table1.setAutoScrollMargin(16)
        self.table1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table1.setProperty("showDropIndicator", True)
        self.table1.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table1.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table1.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table1.setShowGrid(False)
        self.table1.setGridStyle(Qt.NoPen)
        self.table1.setSortingEnabled(False)
        self.table1.setWordWrap(True)
        self.table1.setCornerButtonEnabled(True)
        self.table1.horizontalHeader().setVisible(False)
        self.table1.horizontalHeader().setMinimumSectionSize(10)
        self.table1.horizontalHeader().setDefaultSectionSize(60)
        self.table1.horizontalHeader().setHighlightSections(False)
        self.table1.verticalHeader().setVisible(False)
        self.table1.verticalHeader().setMinimumSectionSize(10)
        self.table1.verticalHeader().setDefaultSectionSize(30)
        self.table1.verticalHeader().setHighlightSections(False)
        self.table2 = QTableWidget(DataTable)
        if (self.table2.columnCount() < 4):
            self.table2.setColumnCount(4)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        if (self.table2.rowCount() < 3):
            self.table2.setRowCount(3)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table2.setVerticalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table2.setVerticalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter);
        self.table2.setVerticalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(0, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(0, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(0, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(0, 3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(1, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(1, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(1, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(1, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(2, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(2, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(2, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.table2.setItem(2, 3, __qtablewidgetitem46)
        self.table2.setObjectName(u"table2")
        self.table2.setEnabled(True)

        sizePolicy.setHeightForWidth(self.table2.sizePolicy().hasHeightForWidth())
        self.table2.setSizePolicy(sizePolicy)
        self.table2.setMinimumSize(QSize(240, 150))
        self.table2.setMaximumSize(QSize(240, 150))
        self.table2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table2.setAutoScroll(False)
        self.table2.setAutoScrollMargin(16)
        self.table2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table2.setProperty("showDropIndicator", True)
        self.table2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table2.setTextElideMode(Qt.ElideRight)
        self.table2.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table2.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table2.setShowGrid(False)
        self.table2.setGridStyle(Qt.NoPen)
        self.table2.setSortingEnabled(False)
        self.table2.setWordWrap(True)
        self.table2.setCornerButtonEnabled(True)
        self.table2.horizontalHeader().setVisible(False)
        self.table2.horizontalHeader().setMinimumSectionSize(10)
        self.table2.horizontalHeader().setDefaultSectionSize(60)
        self.table2.horizontalHeader().setHighlightSections(False)
        self.table2.verticalHeader().setVisible(False)
        self.table2.verticalHeader().setMinimumSectionSize(10)
        self.table2.verticalHeader().setDefaultSectionSize(50)
        self.table2.verticalHeader().setHighlightSections(False)
        self.table3 = QTableWidget(DataTable)
        if (self.table3.columnCount() < 7):
            self.table3.setColumnCount(7)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(5, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(6, __qtablewidgetitem53)
        if (self.table3.rowCount() < 5):
            self.table3.setRowCount(5)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table3.setVerticalHeaderItem(0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table3.setVerticalHeaderItem(1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table3.setVerticalHeaderItem(2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.table3.setVerticalHeaderItem(3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.table3.setVerticalHeaderItem(4, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.table3.setItem(0, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.table3.setItem(0, 1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.table3.setItem(0, 2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.table3.setItem(0, 3, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.table3.setItem(0, 4, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.table3.setItem(0, 5, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.table3.setItem(0, 6, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.table3.setItem(1, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.table3.setItem(1, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.table3.setItem(1, 2, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.table3.setItem(1, 3, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.table3.setItem(1, 4, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.table3.setItem(1, 5, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.table3.setItem(1, 6, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.table3.setItem(2, 0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.table3.setItem(2, 1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.table3.setItem(2, 2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.table3.setItem(2, 3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.table3.setItem(2, 4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.table3.setItem(2, 5, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.table3.setItem(2, 6, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.table3.setItem(3, 0, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.table3.setItem(3, 1, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.table3.setItem(3, 2, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.table3.setItem(3, 3, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.table3.setItem(3, 4, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.table3.setItem(3, 5, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.table3.setItem(3, 6, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.table3.setItem(4, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.table3.setItem(4, 1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.table3.setItem(4, 2, __qtablewidgetitem89)
        self.table3.setObjectName(u"table3")
        self.table3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.table3.sizePolicy().hasHeightForWidth())
        self.table3.setSizePolicy(sizePolicy)
        self.table3.setMinimumSize(QSize(240, 150))
        self.table3.setMaximumSize(QSize(240, 150))
        self.table3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table3.setAutoScroll(False)
        self.table3.setAutoScrollMargin(16)
        self.table3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table3.setProperty("showDropIndicator", True)
        self.table3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table3.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table3.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table3.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table3.setShowGrid(False)
        self.table3.setGridStyle(Qt.NoPen)
        self.table3.setSortingEnabled(False)
        self.table3.setWordWrap(True)
        self.table3.setCornerButtonEnabled(True)
        self.table3.horizontalHeader().setVisible(False)
        self.table3.horizontalHeader().setMinimumSectionSize(10)
        self.table3.horizontalHeader().setDefaultSectionSize(35)
        self.table3.horizontalHeader().setHighlightSections(False)
        self.table3.verticalHeader().setVisible(False)
        self.table3.verticalHeader().setMinimumSectionSize(10)
        self.table3.verticalHeader().setDefaultSectionSize(30)
        self.table3.verticalHeader().setHighlightSections(False)
        self.table4 = QTableWidget(DataTable)
        if (self.table4.columnCount() < 7):
            self.table4.setColumnCount(7)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(2, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(3, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(4, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(5, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(6, __qtablewidgetitem96)
        if (self.table4.rowCount() < 5):
            self.table4.setRowCount(5)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.table4.setVerticalHeaderItem(0, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.table4.setVerticalHeaderItem(1, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.table4.setVerticalHeaderItem(2, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.table4.setVerticalHeaderItem(3, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.table4.setVerticalHeaderItem(4, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.table4.setItem(0, 0, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.table4.setItem(0, 1, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.table4.setItem(0, 2, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.table4.setItem(0, 3, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.table4.setItem(0, 4, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.table4.setItem(0, 5, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.table4.setItem(0, 6, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.table4.setItem(1, 0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.table4.setItem(1, 1, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.table4.setItem(1, 2, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.table4.setItem(1, 3, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.table4.setItem(1, 4, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.table4.setItem(1, 5, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.table4.setItem(1, 6, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.table4.setItem(2, 0, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.table4.setItem(2, 1, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.table4.setItem(2, 2, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.table4.setItem(2, 3, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.table4.setItem(2, 4, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.table4.setItem(2, 5, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.table4.setItem(2, 6, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.table4.setItem(3, 0, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.table4.setItem(3, 1, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.table4.setItem(3, 2, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.table4.setItem(3, 3, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.table4.setItem(3, 4, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.table4.setItem(3, 5, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.table4.setItem(3, 6, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.table4.setItem(4, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.table4.setItem(4, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.table4.setItem(4, 2, __qtablewidgetitem132)
        self.table4.setObjectName(u"table4")
        self.table4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.table4.sizePolicy().hasHeightForWidth())
        self.table4.setSizePolicy(sizePolicy)
        self.table4.setMinimumSize(QSize(240, 150))
        self.table4.setMaximumSize(QSize(240, 150))
        self.table4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table4.setAutoScroll(False)
        self.table4.setAutoScrollMargin(16)
        self.table4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table4.setProperty("showDropIndicator", True)
        self.table4.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table4.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table4.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table4.setShowGrid(False)
        self.table4.setGridStyle(Qt.NoPen)
        self.table4.setSortingEnabled(False)
        self.table4.setWordWrap(True)
        self.table4.setCornerButtonEnabled(True)
        self.table4.horizontalHeader().setVisible(False)
        self.table4.horizontalHeader().setMinimumSectionSize(10)
        self.table4.horizontalHeader().setDefaultSectionSize(35)
        self.table4.horizontalHeader().setHighlightSections(False)
        self.table4.verticalHeader().setVisible(False)
        self.table4.verticalHeader().setMinimumSectionSize(10)
        self.table4.verticalHeader().setDefaultSectionSize(30)
        self.table4.verticalHeader().setHighlightSections(False)
        self.table5 = QTableWidget(DataTable)
        if (self.table5.columnCount() < 7):
            self.table5.setColumnCount(7)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.table5.setHorizontalHeaderItem(0, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.table5.setHorizontalHeaderItem(1, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.table5.setHorizontalHeaderItem(2, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.table5.setHorizontalHeaderItem(3, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.table5.setHorizontalHeaderItem(4, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.table5.setHorizontalHeaderItem(5, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.table5.setHorizontalHeaderItem(6, __qtablewidgetitem139)
        if (self.table5.rowCount() < 5):
            self.table5.setRowCount(5)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.table5.setVerticalHeaderItem(0, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.table5.setVerticalHeaderItem(1, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.table5.setVerticalHeaderItem(2, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.table5.setVerticalHeaderItem(3, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.table5.setVerticalHeaderItem(4, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.table5.setItem(0, 0, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.table5.setItem(0, 1, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.table5.setItem(0, 2, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.table5.setItem(0, 3, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.table5.setItem(0, 4, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.table5.setItem(0, 5, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.table5.setItem(0, 6, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.table5.setItem(1, 0, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.table5.setItem(1, 1, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.table5.setItem(1, 2, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.table5.setItem(1, 3, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.table5.setItem(1, 4, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.table5.setItem(1, 5, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.table5.setItem(1, 6, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.table5.setItem(2, 0, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.table5.setItem(2, 1, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.table5.setItem(2, 2, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.table5.setItem(2, 3, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.table5.setItem(2, 4, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.table5.setItem(2, 5, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.table5.setItem(2, 6, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.table5.setItem(3, 0, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.table5.setItem(3, 1, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.table5.setItem(3, 2, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.table5.setItem(3, 3, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.table5.setItem(3, 4, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.table5.setItem(3, 5, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.table5.setItem(3, 6, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.table5.setItem(4, 0, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.table5.setItem(4, 1, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.table5.setItem(4, 2, __qtablewidgetitem175)
        self.table5.setObjectName(u"table5")
        self.table5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.table5.sizePolicy().hasHeightForWidth())
        self.table5.setSizePolicy(sizePolicy)
        self.table5.setMinimumSize(QSize(240, 150))
        self.table5.setMaximumSize(QSize(240, 150))
        self.table5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table5.setAutoScroll(False)
        self.table5.setAutoScrollMargin(16)
        self.table5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table5.setProperty("showDropIndicator", True)
        self.table5.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table5.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table5.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table5.setShowGrid(False)
        self.table5.setGridStyle(Qt.NoPen)
        self.table5.setSortingEnabled(False)
        self.table5.setWordWrap(True)
        self.table5.setCornerButtonEnabled(True)
        self.table5.horizontalHeader().setVisible(False)
        self.table5.horizontalHeader().setMinimumSectionSize(10)
        self.table5.horizontalHeader().setDefaultSectionSize(35)
        self.table5.horizontalHeader().setHighlightSections(False)
        self.table5.verticalHeader().setVisible(False)
        self.table5.verticalHeader().setMinimumSectionSize(10)
        self.table5.verticalHeader().setDefaultSectionSize(30)
        self.table5.verticalHeader().setHighlightSections(False)
        self.table6 = QTableWidget(DataTable)
        if (self.table6.columnCount() < 7):
            self.table6.setColumnCount(7)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.table6.setHorizontalHeaderItem(0, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.table6.setHorizontalHeaderItem(1, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.table6.setHorizontalHeaderItem(2, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.table6.setHorizontalHeaderItem(3, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.table6.setHorizontalHeaderItem(4, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.table6.setHorizontalHeaderItem(5, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.table6.setHorizontalHeaderItem(6, __qtablewidgetitem182)
        if (self.table6.rowCount() < 5):
            self.table6.setRowCount(5)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.table6.setVerticalHeaderItem(0, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.table6.setVerticalHeaderItem(1, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.table6.setVerticalHeaderItem(2, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.table6.setVerticalHeaderItem(3, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.table6.setVerticalHeaderItem(4, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.table6.setItem(0, 0, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.table6.setItem(0, 1, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.table6.setItem(0, 2, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.table6.setItem(0, 3, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.table6.setItem(0, 4, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.table6.setItem(0, 5, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.table6.setItem(0, 6, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.table6.setItem(1, 0, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.table6.setItem(1, 1, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.table6.setItem(1, 2, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.table6.setItem(1, 3, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.table6.setItem(1, 4, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.table6.setItem(1, 5, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.table6.setItem(1, 6, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.table6.setItem(2, 0, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.table6.setItem(2, 1, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.table6.setItem(2, 2, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.table6.setItem(2, 3, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.table6.setItem(2, 4, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.table6.setItem(2, 5, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.table6.setItem(2, 6, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.table6.setItem(3, 0, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.table6.setItem(3, 1, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.table6.setItem(3, 2, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.table6.setItem(3, 3, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        self.table6.setItem(3, 4, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        self.table6.setItem(3, 5, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.table6.setItem(3, 6, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        self.table6.setItem(4, 0, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        self.table6.setItem(4, 1, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.table6.setItem(4, 2, __qtablewidgetitem218)
        self.table6.setObjectName(u"table6")
        self.table6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.table6.sizePolicy().hasHeightForWidth())
        self.table6.setSizePolicy(sizePolicy)
        self.table6.setMinimumSize(QSize(240, 150))
        self.table6.setMaximumSize(QSize(240, 150))
        self.table6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table6.setAutoScroll(False)
        self.table6.setAutoScrollMargin(16)
        self.table6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table6.setProperty("showDropIndicator", True)
        self.table6.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table6.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table6.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table6.setShowGrid(False)
        self.table6.setGridStyle(Qt.NoPen)
        self.table6.setSortingEnabled(False)
        self.table6.setWordWrap(True)
        self.table6.setCornerButtonEnabled(True)
        self.table6.horizontalHeader().setVisible(False)
        self.table6.horizontalHeader().setMinimumSectionSize(10)
        self.table6.horizontalHeader().setDefaultSectionSize(35)
        self.table6.horizontalHeader().setHighlightSections(False)
        self.table6.verticalHeader().setVisible(False)
        self.table6.verticalHeader().setMinimumSectionSize(10)
        self.table6.verticalHeader().setDefaultSectionSize(30)
        self.table6.verticalHeader().setHighlightSections(False)
        self.line.raise_()
        self.table2.raise_()
        self.table6.raise_()
        self.table4.raise_()
        self.table5.raise_()
        self.table1.raise_()
        self.table3.raise_()

        self.line.setGeometry(QRect(0, 0, 240, 25))
        self.table1.setGeometry(QRect(0, 25, 240, 150))
        self.table2.setGeometry(QRect(0, 25, 240, 150))
        self.table3.setGeometry(QRect(0, 25, 240, 150))
        self.table4.setGeometry(QRect(0, 25, 240, 150))
        self.table5.setGeometry(QRect(0, 25, 240, 150))
        self.table6.setGeometry(QRect(0, 25, 240, 150))

        self.retranslateUi(DataTable)

        self.Y = ''
        self.M = ''
        self.D = ''
        self.table1.hide()
        self.table2.hide()
        self.table3.hide()
        self.table4.hide()
        self.table5.hide()
        self.table6.hide()

        # 绑定signal与slot
        self.line.infocus.connect(self.opentable_1)
        self.line.outfocus.connect(self.closetable)
        self.table1.itemClicked.connect(self.opentable_2)
        self.table2.itemClicked.connect(self.openDtable)
        self.table3.itemClicked.connect(self.lineupdate_31)
        self.table4.itemClicked.connect(self.lineupdate_30)
        self.table5.itemClicked.connect(self.lineupdate_29)
        self.table6.itemClicked.connect(self.lineupdate_28)
        QMetaObject.connectSlotsByName(DataTable)
        # setupUi



    # 控件内容初始化
    def retranslateUi(self, DataTable):
        DataTable.setWindowTitle(QCoreApplication.translate("DataTable", u" ", None))
        ___qtablewidgetitem = self.table1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem1 = self.table1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.table1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem3 = self.table1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem4 = self.table1.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.table1.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.table1.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.table1.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.table1.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.table1.isSortingEnabled()
        self.table1.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.table1.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DataTable", u"2002", None));
        ___qtablewidgetitem10 = self.table1.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DataTable", u"2003", None));
        ___qtablewidgetitem11 = self.table1.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DataTable", u"2004", None));
        ___qtablewidgetitem12 = self.table1.item(0, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DataTable", u"2005", None));
        ___qtablewidgetitem13 = self.table1.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DataTable", u"2006", None));
        ___qtablewidgetitem14 = self.table1.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DataTable", u"2007", None));
        ___qtablewidgetitem15 = self.table1.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("DataTable", u"2008", None));
        ___qtablewidgetitem16 = self.table1.item(1, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("DataTable", u"2009", None));
        ___qtablewidgetitem17 = self.table1.item(2, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("DataTable", u"2010", None));
        ___qtablewidgetitem18 = self.table1.item(2, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("DataTable", u"2011", None));
        ___qtablewidgetitem19 = self.table1.item(2, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("DataTable", u"2012", None));
        ___qtablewidgetitem20 = self.table1.item(2, 3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("DataTable", u"2013", None));
        ___qtablewidgetitem21 = self.table1.item(3, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("DataTable", u"2014", None));
        ___qtablewidgetitem22 = self.table1.item(3, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("DataTable", u"2015", None));
        ___qtablewidgetitem23 = self.table1.item(3, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("DataTable", u"2016", None));
        ___qtablewidgetitem24 = self.table1.item(3, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("DataTable", u"2017", None));
        ___qtablewidgetitem25 = self.table1.item(4, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("DataTable", u"2018", None));
        ___qtablewidgetitem26 = self.table1.item(4, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("DataTable", u"2019", None));
        ___qtablewidgetitem27 = self.table1.item(4, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("DataTable", u"2020", None));
        self.table1.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem28 = self.table2.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem29 = self.table2.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem30 = self.table2.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem31 = self.table2.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem32 = self.table2.verticalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem33 = self.table2.verticalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem34 = self.table2.verticalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled1 = self.table2.isSortingEnabled()
        self.table2.setSortingEnabled(False)
        ___qtablewidgetitem35 = self.table2.item(0, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("DataTable", u"01", None));
        ___qtablewidgetitem36 = self.table2.item(0, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("DataTable", u"02", None));
        ___qtablewidgetitem37 = self.table2.item(0, 2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("DataTable", u"03", None));
        ___qtablewidgetitem38 = self.table2.item(0, 3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("DataTable", u"04", None));
        ___qtablewidgetitem39 = self.table2.item(1, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("DataTable", u"05", None));
        ___qtablewidgetitem40 = self.table2.item(1, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("DataTable", u"06", None));
        ___qtablewidgetitem41 = self.table2.item(1, 2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("DataTable", u"07", None));
        ___qtablewidgetitem42 = self.table2.item(1, 3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("DataTable", u"08", None));
        ___qtablewidgetitem43 = self.table2.item(2, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("DataTable", u"09", None));
        ___qtablewidgetitem44 = self.table2.item(2, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("DataTable", u"10", None));
        ___qtablewidgetitem45 = self.table2.item(2, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("DataTable", u"11", None));
        ___qtablewidgetitem46 = self.table2.item(2, 3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("DataTable", u"12", None));
        self.table2.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem47 = self.table3.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem48 = self.table3.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem49 = self.table3.horizontalHeaderItem(2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem50 = self.table3.horizontalHeaderItem(3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem51 = self.table3.horizontalHeaderItem(4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem52 = self.table3.horizontalHeaderItem(5)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem53 = self.table3.horizontalHeaderItem(6)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem54 = self.table3.verticalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem55 = self.table3.verticalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem56 = self.table3.verticalHeaderItem(2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem57 = self.table3.verticalHeaderItem(3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem58 = self.table3.verticalHeaderItem(4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled2 = self.table3.isSortingEnabled()
        self.table3.setSortingEnabled(False)
        ___qtablewidgetitem59 = self.table3.item(0, 0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("DataTable", u"01", None));
        ___qtablewidgetitem60 = self.table3.item(0, 1)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("DataTable", u"02", None));
        ___qtablewidgetitem61 = self.table3.item(0, 2)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("DataTable", u"03", None));
        ___qtablewidgetitem62 = self.table3.item(0, 3)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("DataTable", u"04", None));
        ___qtablewidgetitem63 = self.table3.item(0, 4)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("DataTable", u"05", None));
        ___qtablewidgetitem64 = self.table3.item(0, 5)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("DataTable", u"06", None));
        ___qtablewidgetitem65 = self.table3.item(0, 6)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("DataTable", u"07", None));
        ___qtablewidgetitem66 = self.table3.item(1, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("DataTable", u"08", None));
        ___qtablewidgetitem67 = self.table3.item(1, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("DataTable", u"09", None));
        ___qtablewidgetitem68 = self.table3.item(1, 2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("DataTable", u"10", None));
        ___qtablewidgetitem69 = self.table3.item(1, 3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("DataTable", u"11", None));
        ___qtablewidgetitem70 = self.table3.item(1, 4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("DataTable", u"12", None));
        ___qtablewidgetitem71 = self.table3.item(1, 5)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("DataTable", u"13", None));
        ___qtablewidgetitem72 = self.table3.item(1, 6)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("DataTable", u"14", None));
        ___qtablewidgetitem73 = self.table3.item(2, 0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("DataTable", u"15", None));
        ___qtablewidgetitem74 = self.table3.item(2, 1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("DataTable", u"16", None));
        ___qtablewidgetitem75 = self.table3.item(2, 2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("DataTable", u"17", None));
        ___qtablewidgetitem76 = self.table3.item(2, 3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("DataTable", u"18", None));
        ___qtablewidgetitem77 = self.table3.item(2, 4)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("DataTable", u"19", None));
        ___qtablewidgetitem78 = self.table3.item(2, 5)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("DataTable", u"20", None));
        ___qtablewidgetitem79 = self.table3.item(2, 6)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("DataTable", u"21", None));
        ___qtablewidgetitem80 = self.table3.item(3, 0)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("DataTable", u"22", None));
        ___qtablewidgetitem81 = self.table3.item(3, 1)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("DataTable", u"23", None));
        ___qtablewidgetitem82 = self.table3.item(3, 2)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("DataTable", u"24", None));
        ___qtablewidgetitem83 = self.table3.item(3, 3)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("DataTable", u"25", None));
        ___qtablewidgetitem84 = self.table3.item(3, 4)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("DataTable", u"26", None));
        ___qtablewidgetitem85 = self.table3.item(3, 5)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("DataTable", u"27", None));
        ___qtablewidgetitem86 = self.table3.item(3, 6)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("DataTable", u"28", None));
        ___qtablewidgetitem87 = self.table3.item(4, 0)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("DataTable", u"29", None));
        ___qtablewidgetitem88 = self.table3.item(4, 1)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("DataTable", u"30", None));
        ___qtablewidgetitem89 = self.table3.item(4, 2)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("DataTable", u"31", None));
        self.table3.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem90 = self.table4.horizontalHeaderItem(0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem91 = self.table4.horizontalHeaderItem(1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem92 = self.table4.horizontalHeaderItem(2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem93 = self.table4.horizontalHeaderItem(3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem94 = self.table4.horizontalHeaderItem(4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem95 = self.table4.horizontalHeaderItem(5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem96 = self.table4.horizontalHeaderItem(6)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem97 = self.table4.verticalHeaderItem(0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem98 = self.table4.verticalHeaderItem(1)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem99 = self.table4.verticalHeaderItem(2)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem100 = self.table4.verticalHeaderItem(3)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem101 = self.table4.verticalHeaderItem(4)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled3 = self.table4.isSortingEnabled()
        self.table4.setSortingEnabled(False)
        ___qtablewidgetitem102 = self.table4.item(0, 0)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("DataTable", u"01", None));
        ___qtablewidgetitem103 = self.table4.item(0, 1)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("DataTable", u"02", None));
        ___qtablewidgetitem104 = self.table4.item(0, 2)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("DataTable", u"03", None));
        ___qtablewidgetitem105 = self.table4.item(0, 3)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("DataTable", u"04", None));
        ___qtablewidgetitem106 = self.table4.item(0, 4)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("DataTable", u"05", None));
        ___qtablewidgetitem107 = self.table4.item(0, 5)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("DataTable", u"06", None));
        ___qtablewidgetitem108 = self.table4.item(0, 6)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("DataTable", u"07", None));
        ___qtablewidgetitem109 = self.table4.item(1, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("DataTable", u"08", None));
        ___qtablewidgetitem110 = self.table4.item(1, 1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("DataTable", u"09", None));
        ___qtablewidgetitem111 = self.table4.item(1, 2)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("DataTable", u"10", None));
        ___qtablewidgetitem112 = self.table4.item(1, 3)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("DataTable", u"11", None));
        ___qtablewidgetitem113 = self.table4.item(1, 4)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("DataTable", u"12", None));
        ___qtablewidgetitem114 = self.table4.item(1, 5)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("DataTable", u"13", None));
        ___qtablewidgetitem115 = self.table4.item(1, 6)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("DataTable", u"14", None));
        ___qtablewidgetitem116 = self.table4.item(2, 0)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("DataTable", u"15", None));
        ___qtablewidgetitem117 = self.table4.item(2, 1)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("DataTable", u"16", None));
        ___qtablewidgetitem118 = self.table4.item(2, 2)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("DataTable", u"17", None));
        ___qtablewidgetitem119 = self.table4.item(2, 3)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("DataTable", u"18", None));
        ___qtablewidgetitem120 = self.table4.item(2, 4)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("DataTable", u"19", None));
        ___qtablewidgetitem121 = self.table4.item(2, 5)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("DataTable", u"20", None));
        ___qtablewidgetitem122 = self.table4.item(2, 6)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("DataTable", u"21", None));
        ___qtablewidgetitem123 = self.table4.item(3, 0)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("DataTable", u"22", None));
        ___qtablewidgetitem124 = self.table4.item(3, 1)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("DataTable", u"23", None));
        ___qtablewidgetitem125 = self.table4.item(3, 2)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("DataTable", u"24", None));
        ___qtablewidgetitem126 = self.table4.item(3, 3)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("DataTable", u"25", None));
        ___qtablewidgetitem127 = self.table4.item(3, 4)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("DataTable", u"26", None));
        ___qtablewidgetitem128 = self.table4.item(3, 5)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("DataTable", u"27", None));
        ___qtablewidgetitem129 = self.table4.item(3, 6)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("DataTable", u"28", None));
        ___qtablewidgetitem130 = self.table4.item(4, 0)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("DataTable", u"29", None));
        ___qtablewidgetitem131 = self.table4.item(4, 1)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("DataTable", u"30", None));
        self.table4.setSortingEnabled(__sortingEnabled3)

        ___qtablewidgetitem132 = self.table5.horizontalHeaderItem(0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem133 = self.table5.horizontalHeaderItem(1)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem134 = self.table5.horizontalHeaderItem(2)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem135 = self.table5.horizontalHeaderItem(3)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem136 = self.table5.horizontalHeaderItem(4)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem137 = self.table5.horizontalHeaderItem(5)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem138 = self.table5.horizontalHeaderItem(6)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem139 = self.table5.verticalHeaderItem(0)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem140 = self.table5.verticalHeaderItem(1)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem141 = self.table5.verticalHeaderItem(2)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem142 = self.table5.verticalHeaderItem(3)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem143 = self.table5.verticalHeaderItem(4)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled4 = self.table5.isSortingEnabled()
        self.table5.setSortingEnabled(False)
        ___qtablewidgetitem144 = self.table5.item(0, 0)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("DataTable", u"01", None));
        ___qtablewidgetitem145 = self.table5.item(0, 1)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("DataTable", u"02", None));
        ___qtablewidgetitem146 = self.table5.item(0, 2)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("DataTable", u"03", None));
        ___qtablewidgetitem147 = self.table5.item(0, 3)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("DataTable", u"04", None));
        ___qtablewidgetitem148 = self.table5.item(0, 4)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("DataTable", u"05", None));
        ___qtablewidgetitem149 = self.table5.item(0, 5)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("DataTable", u"06", None));
        ___qtablewidgetitem150 = self.table5.item(0, 6)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("DataTable", u"07", None));
        ___qtablewidgetitem151 = self.table5.item(1, 0)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("DataTable", u"08", None));
        ___qtablewidgetitem152 = self.table5.item(1, 1)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("DataTable", u"09", None));
        ___qtablewidgetitem153 = self.table5.item(1, 2)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("DataTable", u"10", None));
        ___qtablewidgetitem154 = self.table5.item(1, 3)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("DataTable", u"11", None));
        ___qtablewidgetitem155 = self.table5.item(1, 4)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("DataTable", u"12", None));
        ___qtablewidgetitem156 = self.table5.item(1, 5)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("DataTable", u"13", None));
        ___qtablewidgetitem157 = self.table5.item(1, 6)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("DataTable", u"14", None));
        ___qtablewidgetitem158 = self.table5.item(2, 0)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("DataTable", u"15", None));
        ___qtablewidgetitem159 = self.table5.item(2, 1)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("DataTable", u"16", None));
        ___qtablewidgetitem160 = self.table5.item(2, 2)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("DataTable", u"17", None));
        ___qtablewidgetitem161 = self.table5.item(2, 3)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("DataTable", u"18", None));
        ___qtablewidgetitem162 = self.table5.item(2, 4)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("DataTable", u"19", None));
        ___qtablewidgetitem163 = self.table5.item(2, 5)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("DataTable", u"20", None));
        ___qtablewidgetitem164 = self.table5.item(2, 6)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("DataTable", u"21", None));
        ___qtablewidgetitem165 = self.table5.item(3, 0)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("DataTable", u"22", None));
        ___qtablewidgetitem166 = self.table5.item(3, 1)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("DataTable", u"23", None));
        ___qtablewidgetitem167 = self.table5.item(3, 2)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("DataTable", u"24", None));
        ___qtablewidgetitem168 = self.table5.item(3, 3)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("DataTable", u"25", None));
        ___qtablewidgetitem169 = self.table5.item(3, 4)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("DataTable", u"26", None));
        ___qtablewidgetitem170 = self.table5.item(3, 5)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("DataTable", u"27", None));
        ___qtablewidgetitem171 = self.table5.item(3, 6)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("DataTable", u"28", None));
        ___qtablewidgetitem172 = self.table5.item(4, 0)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("DataTable", u"29", None));
        self.table5.setSortingEnabled(__sortingEnabled4)

        ___qtablewidgetitem173 = self.table6.horizontalHeaderItem(0)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem174 = self.table6.horizontalHeaderItem(1)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem175 = self.table6.horizontalHeaderItem(2)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem176 = self.table6.horizontalHeaderItem(3)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem177 = self.table6.horizontalHeaderItem(4)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem178 = self.table6.horizontalHeaderItem(5)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem179 = self.table6.horizontalHeaderItem(6)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem180 = self.table6.verticalHeaderItem(0)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem181 = self.table6.verticalHeaderItem(1)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem182 = self.table6.verticalHeaderItem(2)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem183 = self.table6.verticalHeaderItem(3)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem184 = self.table6.verticalHeaderItem(4)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("DataTable", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled5 = self.table6.isSortingEnabled()
        self.table6.setSortingEnabled(False)
        ___qtablewidgetitem185 = self.table6.item(0, 0)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("DataTable", u"01", None));
        ___qtablewidgetitem186 = self.table6.item(0, 1)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("DataTable", u"02", None));
        ___qtablewidgetitem187 = self.table6.item(0, 2)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("DataTable", u"03", None));
        ___qtablewidgetitem188 = self.table6.item(0, 3)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("DataTable", u"04", None));
        ___qtablewidgetitem189 = self.table6.item(0, 4)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("DataTable", u"05", None));
        ___qtablewidgetitem190 = self.table6.item(0, 5)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("DataTable", u"06", None));
        ___qtablewidgetitem191 = self.table6.item(0, 6)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("DataTable", u"07", None));
        ___qtablewidgetitem192 = self.table6.item(1, 0)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("DataTable", u"08", None));
        ___qtablewidgetitem193 = self.table6.item(1, 1)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("DataTable", u"09", None));
        ___qtablewidgetitem194 = self.table6.item(1, 2)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("DataTable", u"10", None));
        ___qtablewidgetitem195 = self.table6.item(1, 3)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("DataTable", u"11", None));
        ___qtablewidgetitem196 = self.table6.item(1, 4)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("DataTable", u"12", None));
        ___qtablewidgetitem197 = self.table6.item(1, 5)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("DataTable", u"13", None));
        ___qtablewidgetitem198 = self.table6.item(1, 6)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("DataTable", u"14", None));
        ___qtablewidgetitem199 = self.table6.item(2, 0)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("DataTable", u"15", None));
        ___qtablewidgetitem200 = self.table6.item(2, 1)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("DataTable", u"16", None));
        ___qtablewidgetitem201 = self.table6.item(2, 2)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("DataTable", u"17", None));
        ___qtablewidgetitem202 = self.table6.item(2, 3)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("DataTable", u"18", None));
        ___qtablewidgetitem203 = self.table6.item(2, 4)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("DataTable", u"19", None));
        ___qtablewidgetitem204 = self.table6.item(2, 5)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("DataTable", u"20", None));
        ___qtablewidgetitem205 = self.table6.item(2, 6)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("DataTable", u"21", None));
        ___qtablewidgetitem206 = self.table6.item(3, 0)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("DataTable", u"22", None));
        ___qtablewidgetitem207 = self.table6.item(3, 1)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("DataTable", u"23", None));
        ___qtablewidgetitem208 = self.table6.item(3, 2)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("DataTable", u"24", None));
        ___qtablewidgetitem209 = self.table6.item(3, 3)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("DataTable", u"25", None));
        ___qtablewidgetitem210 = self.table6.item(3, 4)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("DataTable", u"26", None));
        ___qtablewidgetitem211 = self.table6.item(3, 5)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("DataTable", u"27", None));
        ___qtablewidgetitem212 = self.table6.item(3, 6)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("DataTable", u"28", None));
        self.table6.setSortingEnabled(__sortingEnabled5)

    # 关闭年表格
    def closetable(self):
        self.table1.hide()
        self.table1.clearSelection()

    # 打开年表格，关闭其他表格
    def opentable_1(self):
        self.table1.show()
        self.table2.hide()
        self.table3.hide()
        self.table4.hide()
        self.table5.hide()
        self.table6.hide()

    # 打开月表格
    def opentable_2(self):
        self.Y = self.table1.selectedItems()[0].text()
        self.table1.hide()
        self.table1.clearSelection()
        self.line.setText(self.Y )
        self.table2.show()

    # 打开日表格
    def openDtable(self):
        self.M = self.table2.selectedItems()[0].text()
        self.table2.hide()
        self.table2.clearSelection()
        self.line.setText(self.Y + '-' + self.M )
        if self.M in ['01' , '03' , '05' , '07' , '08' , '10' , '12']:
            self.table3.show()
        elif self.M in [ '04' , '06' , '09' , '11']:
            self.table4.show()
        else:
            if int(self.Y) % 4 == 0:
                self.table5.show()
            else:
                self.table6.show()

    # 文本显示
    def lineupdate_31(self):
        self.D = self.table3.selectedItems()[0].text()
        self.table3.hide()
        self.table3.clearSelection()
        self.line.setText(self.Y + '-' + self.M + '-' + self.D)
    def lineupdate_30(self):
        self.D = self.table4.selectedItems()[0].text()
        self.table4.hide()
        self.table4.clearSelection()
        self.line.setText(self.Y + '-' + self.M + '-' + self.D)
    def lineupdate_29(self):
        self.D = self.table5.selectedItems()[0].text()
        self.table5.hide()
        self.table5.clearSelection()
        self.line.setText(self.Y + '-' + self.M + '-' + self.D)
    def lineupdate_28(self):
        self.D = self.table6.selectedItems()[0].text()
        self.table6.hide()
        self.table6.clearSelection()
        self.line.setText(self.Y + '-' + self.M + '-' + self.D)
