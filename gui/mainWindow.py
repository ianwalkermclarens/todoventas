import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QDialog, QDialogButtonBox, QMainWindow
from gui.interfaces.uix_mainWindow import Ui_MainWindow


basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        
