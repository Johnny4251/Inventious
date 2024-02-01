from app.state_controller.Events import Event
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QPushButton , QFrame)

class CenterContentState:
    def __content_title(self):
        main_content = QLabel("Select an action from the left side panel")
        main_content.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        
        return main_content
    
    def __content_dataset(self):
        main_content = QLabel("Create Dataset Area")
        main_content.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        
        return main_content
    
    def get_content(self, event):

        match event:
            case Event.TITLE:
                main_content = self.__content_title()
            case Event.CREATE_DATASET:
                main_content = self.__content_dataset()


        return main_content
    
    

    
