from librery.db import database
from PyQt6.QtWidgets import QComboBox
import json


class control_combobox():
    def __init__(self,param1="",param2="",param3=""):
        self.dbs = database()
        pass

    def loadEstados(self,obj:QComboBox,param=""):
        querys = "select * from cat_estados"
        resultado = self.dbs.getRows(querys)
        if resultado!=None:
            obj.clear()
            infoEstados = json.loads(resultado)
            obj.addItem(param)
            for valueEstados in infoEstados:
                obj.addItem(valueEstados["estado"])
    
            #obj.setCurrentText(param)
                
    def loadMunicipios(self,obj:QComboBox,param1="",param2=""):
        if param1=="":
            obj.clear()
        else:
            querys = f"select cat_municipios.municipio from cat_estados,cat_municipios where cat_estados.estado='{param1}' and cat_estados.idestado=cat_municipios.idestado;"

            resultado = self.dbs.getRows(querys)
            if resultado!=None:
                obj.clear()
                infoMunicipios = json.loads(resultado)
                obj.addItem(param2)
                for valueMunicipios in infoMunicipios:
                    obj.addItem(valueMunicipios["municipio"])

    def loadColonia(self,obj:QComboBox,param1="",param2="",param3=""):
        if param1=="" and param2=="":
            obj.clear()
        else:
            querys = f"select cat_cp.colonia from cat_estados,cat_municipios,cat_cp where cat_estados.estado='{param1}' and cat_estados.idestado=cat_municipios.idestado and cat_municipios.municipio='{param2}' and cat_cp.idestado=cat_estados.idestado and cat_cp.idmunicipio=cat_municipios.idmunicipio  order by cat_cp.colonia;"

            resultado = self.dbs.getRows(querys)
            if resultado!=None:
                obj.clear()
                infoColonias = json.loads(resultado)
                obj.addItem(param3)
                for valueColonias in infoColonias:
                    obj.addItem(valueColonias["colonia"])

    def loadCP(self,obj:QComboBox,param1="",param2="",param3="",param4=""):
        if param1=="" and param2=="" and param3=="":
            obj.clear()
        else:
            querys = f"select cat_cp.cp from cat_estados,cat_municipios,cat_cp where cat_estados.estado='{param1}' and cat_estados.idestado=cat_municipios.idestado and cat_municipios.municipio='{param2}' and cat_cp.idestado=cat_estados.idestado and cat_cp.idmunicipio=cat_municipios.idmunicipio and cat_cp.colonia='{param3}' order by cat_cp.colonia;"
            print(querys)
            resultado = self.dbs.getRows(querys)
            if resultado!=None:
                obj.clear()
                infoColonias = json.loads(resultado)
                obj.addItem(param4)
                for valueColonias in infoColonias:
                    obj.addItem(str(valueColonias["cp"]))


