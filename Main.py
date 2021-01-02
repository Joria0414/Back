from PySide2.QtWidgets import QApplication
from MainWindow import MainWindow

def main():
    app = QApplication([])
    mainwindow = MainWindow()
    mainwindow.ui.dataline.setText("600000")
    mainwindow.ui.strategyline.setText("双均线策略")
    mainwindow.ui.cashline.setText("100000")
    mainwindow.ui.datebegin.ui.line.setText("2020-01-01")
    mainwindow.ui.dateend.ui.line.setText("2020-12-12")
    mainwindow.show()
    app.exec_()

if __name__ == '__main__':
    main()