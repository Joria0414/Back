#
# 回测结果详情展示窗口
#
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# 回测结果详情展示窗口控件
class DetailsWindow(QWidget):
    # 参数figure：展示图片，log：展示日志
    def __init__(self,figure,log):
        super().__init__()
        self.setupUi()
        self.plot(figure,log)

    # UI
    def setupUi(self,):
        self.resize(1127, 728)
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(12)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 20)

        self.retranslateUi()

    # 画图
    def plot(self,figure,log):
        self.canvas = FigureCanvas(figure)

        self.verticalLayout.addWidget(self.canvas)

        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumHeight(180)
        self.plainTextEdit.setFocusPolicy(Qt.NoFocus)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setMaximumBlockCount(0)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setPlainText(log)

        self.verticalLayout.addWidget(self.plainTextEdit)

    def retranslateUi(self):
        self.setWindowTitle("策略详情")