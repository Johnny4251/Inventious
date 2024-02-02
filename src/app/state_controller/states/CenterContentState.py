from app.state_controller.Events import Event
import Utils
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QPushButton , QFrame, QFileDialog, QSpinBox,
                             QCheckBox)
from tensorflow.keras.layers.experimental import preprocessing

class CenterContentState:

    def __content_title(self):
        main_content = QLabel("Select an action from the left side panel")
        main_content.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        
        return main_content
    
    def __content_transform_creation(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.horizontal_flip_label = QLabel("Horizontal Flip: ")
        self.horizontal_flip_checkbox = QCheckBox()
        layout.addWidget(self.horizontal_flip_label)
        layout.addWidget(self.horizontal_flip_checkbox)

        self.vertical_flip_label = QLabel("Vertical Flip: ")
        self.vertical_flip_checkbox = QCheckBox()
        layout.addWidget(self.vertical_flip_label)
        layout.addWidget(self.vertical_flip_checkbox)

        self.rotation_label = QLabel("Random Rotation (degrees): ")
        self.rotation_spinbox = QSpinBox()
        self.rotation_spinbox.setMinimum(0)
        self.rotation_spinbox.setMaximum(360)
        layout.addWidget(self.rotation_label)
        layout.addWidget(self.rotation_spinbox)

        self.shuffle_label = QLabel("Shuffle: ")
        self.shuffle_checkbox = QCheckBox()
        layout.addWidget(self.shuffle_label)
        layout.addWidget(self.shuffle_checkbox)

        self.random_crop_label = QLabel("Random Cropping (percentage): ")
        self.random_crop_spinbox = QSpinBox()
        self.random_crop_spinbox.setMinimum(0)
        self.random_crop_spinbox.setMaximum(100)
        layout.addWidget(self.random_crop_label)
        layout.addWidget(self.random_crop_spinbox)

        self.confirm_btn = QPushButton("Confirm Transformation")
        self.confirm_btn.clicked.connect(self.create_transformation_object)
        layout.addWidget(self.confirm_btn)

        return widget

    def create_transformation_object(self):
        Utils.data_augmentation_layers = [
            preprocessing.RandomFlip("horizontal" if self.horizontal_flip_checkbox.isChecked() else "none"),
            preprocessing.RandomFlip("vertical" if self.vertical_flip_checkbox.isChecked() else "none"),
            preprocessing.RandomRotation(self.rotation_spinbox.value() / 360.0),
        ]

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
                return self.__content_title()
            case Event.CREATE_DATASET:
                return self.__content_dataset_creation()
            case Event.CREATE_TRANSFORM:
                return self.__content_transform_creation()

    

    
