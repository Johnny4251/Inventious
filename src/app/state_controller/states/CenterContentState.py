from app.state_controller.Events import Event
import Utils
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QPushButton , QFrame, QFileDialog)

class CenterContentState:

    # Title Content Handler
    def __content_title(self):
        main_content = QLabel("Select an action from the left side panel")
        main_content.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        
        return main_content
    
    def __content_dataset_creation(self):
        # Create the main widget and layout for this content
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Create labels
        self.train_dir_label = QLabel("Training Directory: " + Utils.train_dir_loc)
        self.test_dir_label = QLabel("Testing Directory: " + Utils.test_dir_loc)

        # Create buttons and connect them to methods for opening file dialog
        train_dir_btn = QPushButton("Select Training Directory")
        train_dir_btn.clicked.connect(lambda: self.open_file_dialog(self.train_dir_label))

        test_dir_btn = QPushButton("Select Testing Directory")
        test_dir_btn.clicked.connect(lambda: self.open_file_dialog(self.test_dir_label))

        # Add widgets to the layout
        layout.addWidget(self.train_dir_label)
        layout.addWidget(train_dir_btn)
        layout.addWidget(self.test_dir_label)
        layout.addWidget(test_dir_btn)

        return widget

    def open_file_dialog(self, label):
        # Open a directory selection dialog
        directory = QFileDialog.getExistingDirectory(None, "Select Directory")
        if directory:  # Update label text if a directory was selected
            label.setText(f"Selected Directory: {directory}")

        if label == self.test_dir_label:
            Utils.test_dir_loc = directory
        elif label == self.train_dir_label:
            Utils.train_dir_loc = directory

    def get_content(self, event):

        match event:
            case Event.TITLE:
                main_content = self.__content_title()
            case Event.CREATE_DATASET:
                main_content = self.__content_dataset_creation()


        return main_content
    
    

    
