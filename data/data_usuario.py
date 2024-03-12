from librery.db import database
from model.model_usuario import model_usuario

class data_usuario():
    def __init__(self):
        self.dbs = database()

    def login(self,usuario:model_usuario):
        respuesta = self.dbs.getRows(f"select usuarios.idkey,usuarios.nombre_usuario,usuarios.username,tipo_usuarios.nombre,usuarios.idkey_tipo_usuarios from usuarios,tipo_usuarios where usuarios.username='{usuario.username}' and usuarios.passw='{usuario.password}' and usuarios.idkey_tipo_usuarios=tipo_usuarios.idkey;")
        return respuesta



