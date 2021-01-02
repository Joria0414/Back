import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from pylab import *
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QThread, Signal


class MyThread(QThread):
    mysignal =Signal()
    def __init__(self):
        super().__init__()
    def setup(self,i):
        self.i = i
    def run(self):
        for i in range(self.i):
            print(i)
            time.sleep(1)
        self.mysignal.emit()
        pass

class ResultWindow(QWidget):
    def __init__(self, parent=None):
        # 父类初始化方法
        super(ResultWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.mythread = MyThread()
        self.mythread.mysignal.connect(self.closeThread)
        self.setWindowTitle('回测结果')
        self.setGeometry(300,200,1200,700)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 10, 20, 50)
        self.button = QPushButton()
        self.layout.addWidget(self.button)
        self.button2 = QPushButton()
        self.layout.addWidget(self.button2)
        self.button.setText("asasada")
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.openThread)
        self.button2.clicked.connect(self.closeThread)

    def openThread(self):

        self.mythread.setup(5)

        if not self.mythread.isRunning():
            self.mythread.start()

    def closeThread(self):
        # self.mythread.terminate()
        print(1111111)

def main():
    app = QApplication([])
    mainwindow = ResultWindow()
    mainwindow.show()
    app.exec_()

if __name__ == '__main__':
    main()