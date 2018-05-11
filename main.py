#!/usr/bin/python3

"""
create ui_mainwindow.py
pyuic5 mainwindow.ui > ui_mainwindow.py
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
        QMessageBox, QTextEdit)

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.title = 'PyQt5 simple window - pythonspot.com'
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.show()
 
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
