from app.state_controller.Events import Event
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QPushButton , QFrame)

class CenterContentState:
    def get_content(self, event):

        main_content = QLabel("Main Content Area")
        main_content.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        return main_content

    