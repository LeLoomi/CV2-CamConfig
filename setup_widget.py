from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import pyqtSignal

class SetupWidget(QWidget):
    
    configuration_completed = pyqtSignal(str, str)
    
    def __init__(self):
        super().__init__()
        
        main_layout = QHBoxLayout()
        content_layout = QVBoxLayout()
        
        testLabel = QLabel()
        testLabel.setText('I am a test label for the setup screen :3')
        
        testButton = QPushButton()
        testButton.setText('Next')
        testButton.clicked.connect(self.handle_setup)
        
        content_layout.addStretch()
        content_layout.addWidget(testLabel)
        content_layout.addWidget(testButton)
        content_layout.addStretch()
        
        main_layout.addStretch()
        main_layout.addLayout(content_layout)
        main_layout.addStretch()
        
        self.setLayout(main_layout)
    
    def handle_setup(self):
        self.configuration_completed.emit('test text 1', 'test text 2')