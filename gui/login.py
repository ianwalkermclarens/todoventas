import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QDialog, QDialogButtonBox
from data.data_usuario import data_usuario
from gui.mainWindow import MainWindow
from model.model_usuario import model_usuario
from gui.interfaces.uix_login import Ui_uix_login
from librery.alerts import alerts


basedir = os.path.dirname(__file__)

class Login(QDialog,Ui_uix_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnAcceder.clicked.connect(self.ingresar)
        #self.btnAcceder.clicked.connect(self.ingresar)
        self.show()

    def ingresar(self):
        if self.txtUser.text()=="":
            alerts("Introduzca el nombre del usuario")
            self.txtUser.setFocus()
        elif self.txtPassword.text()=="":
            alerts("Introduzca la contraseña del usuario")
            self.txtPassword.setFocus()
        else:
            modelo_usuario = model_usuario(nombre_usuario="",username=self.txtUser.text(),password=self.txtPassword.text())
            datos_usuario=data_usuario()
            respuesta = datos_usuario.login(modelo_usuario)
            


            #self.main = MainWindow()
            #self.close()


    def initGUI(self):
        pass

        