import sys
import Utils
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class TitleState():
    def render(self):
        if Utils.DEBUG_MODE: print("rendering title..")
        self.app = QApplication(sys.argv)
        self.win = MainWindow()
        self.win.show()
        self.app.exec_()
        if Utils.DEBUG_MODE: print("title rendered..")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def button_clicked(self):
        print("clicked")

    def initUI(self):
        self.setGeometry(200, 200, 1024, 640)
        self.setWindowTitle("Inventious")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("A label")
        self.label.move(100,100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.button_clicked)
