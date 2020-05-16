import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QTimer
import time

class HelloWindow(QMainWindow):

    def handleTimer(self):
        localtime = time.asctime(time.localtime(time.time()))
        self.timeLab.setText(localtime)

    def __init__(self):
        QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)

        self.timeLab = QLabel(self)
        # self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("CSU Global")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        localtime = time.asctime(time.localtime(time.time()))

        self.timeLab = QLabel('Pending Time', self)
        self.timeLab.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.timeLab, 0, 0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start (1000)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()

    mainWin.show()
    sys.exit( app.exec_() )
