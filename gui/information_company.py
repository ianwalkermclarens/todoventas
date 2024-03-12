from PyQt6.QtWidgets import QDialog
from gui.interfaces.uix_information_company import Ui_uix_information_company
from librery.alerts import alerts
from librery.db import database
import json
from librery.input_datas import *
from librery.control_combobox import control_combobox


class information_company(QDialog,Ui_uix_information_company):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.combos = control_combobox()
        
        self.txtRSocial.setValidator(input_datasTXT())
        self.txtRFC.setValidator(input_datasRFC())
        self.txtRFC.textChanged.connect(self.uppData)
        self.txtDireccion.setValidator(input_datasTXT())
        self.comboMunicipio.setValidator(input_datasNothing())
        self.comboColonia.setValidator(input_datasNothing())
        self.comboCodigoPostal.setValidator(input_datasNothing())

        self.combos.loadEstados(self.comboEstado,"")
        self.comboEstado.currentIndexChanged.connect(self.cambioEstado)
        self.comboMunicipio.currentIndexChanged.connect(self.cambioMunicipio)
        self.comboColonia.currentIndexChanged.connect(self.cambioColonia)        
        self.setModal(True)
        self.show()

    def uppData(self,s):
        self.txtRFC.setText(self.txtRFC.text().upper())

    def cambioEstado(self,indice):
        self.combos.loadMunicipios(self.comboMunicipio,self.comboEstado.currentText(),"")

    def cambioMunicipio(self,indice):
        self.combos.loadColonia(self.comboColonia,self.comboEstado.currentText(),self.comboMunicipio.currentText(),"")

    def cambioColonia(self,indice):
        self.combos.loadCP(self.comboCodigoPostal,self.comboEstado.currentText(),self.comboMunicipio.currentText(),self.comboColonia.currentText(),"")
