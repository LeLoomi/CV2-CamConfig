import cv2 as cv
from PyQt6.QtWidgets import QApplication, QMainWindow
from setup_widget import SetupWidget
from config_widget import ConfigWidget

class MainWindow(QMainWindow):
    
    def __init__(self):
        print('[CamConfig] Booting up')
        super().__init__()
        
        # window setup
        self.showMaximized()
        self.setWindowTitle('CV2 CamConfig')
        
        # initial entry
        self.show_setup_widget()
    
    def show_setup_widget(self):
        print('[CamConfig] Showing setup screen')
        setup_widget = SetupWidget()
        setup_widget.configuration_completed.connect(self.show_configuration_widget)
        self.setCentralWidget(setup_widget)

    def show_configuration_widget(self):
        print('[CamConfig] Showing configuration screen')
        config_widget = ConfigWidget()
        self.setCentralWidget(config_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()