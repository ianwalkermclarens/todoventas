import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QDialog, QDialogButtonBox
#from data.usuario import UsuarioData
from gui.mainWindow import MainWindow
#from model.usuario import Usuario
from gui.interfaces.uix_login import Ui_uix_login

basedir = os.path.dirname(__file__)

class Login(QDialog,Ui_uix_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnAcceder.clicked.connect(self.ingresar)
        #self.btnAcceder.clicked.connect(self.ingresar)
        self.show()

    def ingresar(self):
        self.main = MainWindow()
        self.close()
        #print("hola")

    def initGUI(self):
        pass

        