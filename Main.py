import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QTimer
import time


class HelloWindow ( QMainWindow ) :

    def handleTimer(self) :
        localtime = time.asctime ( time.localtime ( time.time () ) )
        self.timeLab.setText ( localtime )

    def __init__(self) :
        self.SetMainStyle()

        self.setWindowTitle ( "CSU" )

        central_widget = QWidget ( self )
        self.setCentralWidget ( central_widget )

        grid_layout = QGridLayout ( self )
        central_widget.setLayout ( grid_layout )

        self.CreateTimeDisplay ( grid_layout )
        self.SetDateDisplayStyles ()
        self.SetSize ()
        self.StartTimeUpdates ()

    def SetMainStyle(self):
        QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)

    def CreateTimeDisplay(self, grid_layout) :
        self.timeLab = QLabel ( 'Pending Time', self )
        self.timeLab.setFont(QtGui.QFont('SansSerif', 18))
        self.timeLab.setAlignment ( QtCore.Qt.AlignCenter )
        grid_layout.addWidget ( self.timeLab, 0, 0 )

    def SetDateDisplayStyles(self) :
        self.timeLab.setStyleSheet ( "background-color: yellow;border: 1px solid" )

    def SetSize(self) :
        localtime = time.asctime ( time.localtime ( time.time () ) )
        metrics = QtGui.QFontMetrics ( self.timeLab.font () )
        twidth = metrics.boundingRect ( localtime ).width ()
        theight = metrics.boundingRect ( localtime ).height ()

        self.setMinimumWidth ( twidth )
        self.setMaximumHeight ( theight )

    def StartTimeUpdates(self) :
        self.timer = QTimer ()
        self.timer.timeout.connect ( self.handleTimer )
        self.timer.start ( 1000 )

    def StopTimeUpdates(self) :
        self.timer.stop ()

if __name__ == "__main__" :
    app = QtWidgets.QApplication ( sys.argv )
    mainWin = HelloWindow ()

    mainWin.show ()

    sys.exit ( app.exec_ () )
