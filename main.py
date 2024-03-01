from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

from gui.login import Login
import sys
import os

basedir = os.path.dirname(__file__)

class AppMain():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setWindowIcon(QIcon(os.path.join(basedir, "icons", "icon.svg")))
        self.login = Login()
        super().__init__()
        self.app.exec()

app = AppMain()