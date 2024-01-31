import sys
import Utils
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QPushButton , QFrame)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('src\\app\\logo.png'))
        self.setWindowTitle(Utils.WINDOW_NAME)
        self.initUI()
    
    def initUI(self):

        self.setMinimumSize(Utils.WINDOW_MIN_X, Utils.WINDOW_MIN_Y)
        self.setMaximumSize(Utils.WINDOW_MAX_X,Utils.WINDOW_MAX_Y)
        self.resize(Utils.WINDOW_MAX_X,Utils.WINDOW_MAX_Y)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout(main_widget)

        header = self.create_header()
        main_layout.addWidget(header)

        lower_layout = QHBoxLayout()

        left_panel = self.create_left_panel()
        lower_layout.addWidget(left_panel)

        main_content = QLabel("Main Content Area")
        main_content.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        lower_layout.addWidget(main_content)

        main_layout.addLayout(lower_layout)

    
    def create_header(self):
        # Create the logo label
        logo = QLabel()
        pixmap = QPixmap('src\\app\\bannerlogo.png')
        logo.setPixmap(pixmap.scaledToHeight(Utils.HEADER_HEIGHT, Qt.SmoothTransformation))

        # Set the fixed height for the logo label
        logo.setFixedHeight(Utils.HEADER_HEIGHT)

        return logo

    def create_left_panel(self):
        panel = QWidget()
        panel.setFixedWidth(Utils.LEFT_PANEL_WIDTH)
        panel_layout = QVBoxLayout(panel)

        create_dset_btn = QPushButton("Create Dataset")
        create_transform_btn = QPushButton("Create Transform")
        select_model_btn = QPushButton("Create Transform")
        train_model_btn = QPushButton("Train Model")

        panel_btns = [create_dset_btn, create_transform_btn, 
                   select_model_btn, train_model_btn]
        for btn in panel_btns:
            panel_layout.addWidget(btn)

        return panel