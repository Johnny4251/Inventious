import sys
import Utils
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QPushButton , QFrame)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from app.state_controller.Events import Event
from app.state_controller.states.CenterContentState import CenterContentState


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Add Window Icon, initialize UI
        self.setWindowIcon(QtGui.QIcon('src\\app\\logo.png'))
        self.setWindowTitle(Utils.WINDOW_NAME)
        self.initUI()
    
    # Renders initial state of UI
    def initUI(self):

        # Window size preferences
        self.setMinimumSize(Utils.WINDOW_MIN_X, Utils.WINDOW_MIN_Y)
        self.setMaximumSize(Utils.WINDOW_MAX_X,Utils.WINDOW_MAX_Y)
        self.resize(Utils.WINDOW_MAX_X,Utils.WINDOW_MAX_Y)

        # Create main widget
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout(self.main_widget)

        # Header is returned by self.create_header()
        header = self.create_header()
        self.main_layout.addWidget(header)
        
        self.lower_layout = QHBoxLayout()

        # Left panel is returned by self.create_left_panel()
        left_panel = self.create_left_panel()
        self.lower_layout.addWidget(left_panel)

        # Center content is handeld & returned by the CenterContentState class
        self.center_content = CenterContentState().get_content(Event.TITLE)
        self.lower_layout.addWidget(self.center_content)

        self.main_layout.addLayout(self.lower_layout)

    def create_dataset_pressed(self):
        # Remove the old content from the layout
        old_content = self.center_content
        old_content.setParent(None)

        # Create and display the new dataset creation content
        self.center_content = CenterContentState().get_content(Event.CREATE_DATASET)
        self.lower_layout.addWidget(self.center_content)
        if Utils.DEBUG_MODE:
            print("create dataset button pressed")

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
        create_dset_btn.clicked.connect(self.create_dataset_pressed)

        create_transform_btn = QPushButton("Create Transform")
        select_model_btn = QPushButton("Create Transform")
        train_model_btn = QPushButton("Train Model")

        panel_btns = [create_dset_btn, create_transform_btn, 
                   select_model_btn, train_model_btn]
        for btn in panel_btns:
            panel_layout.addWidget(btn)

        return panel