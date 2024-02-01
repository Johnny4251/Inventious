import sys
import Utils
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QPushButton , QFrame)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from app.state_controller.states.MainWindow import MainWindow

class TitleState():
    def render(self):
        if Utils.DEBUG_MODE: print("rendering title..")
        self.app = QApplication(sys.argv)

        style_path = 'src\\app\\darktheme.css'
        try:
            with open(style_path, "r") as f:
                self.app.setStyleSheet(f.read())
        except Exception as e:
            print("Exception caught when trying to open "+style_path, e)

        self.win = MainWindow()
        self.win.show()
        self.app.exec_()
        if Utils.DEBUG_MODE: print("title rendered..")