from PyQt6.QtWidgets import QApplication
from gui.login import Login
import sys

class AppMain():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login = Login()
        super().__init__()
        self.app.exec()

app = AppMain()