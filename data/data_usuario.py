from librery.db import database
from model.model_usuario import model_usuario
from librery.db import database

class data_usuario():
    def __init__(self):
        self.dbs = database()

    def login(self,usuario:model_usuario):
        print("llega la informacion al login en data =",usuario.username,usuario.password)
        respuesta = self.dbs.getRows("select usuarios.idkey,usuarios.nombre_usuario,usuarios.username,tipo_usuarios.nombre,tipo_usuarios.idkey from usuarios,tipo_usuarios where usuarios.username='admin' and usuarios.passw='admin' and usuarios.idkey_tipo_usuarios=tipo_usuarios.idkey;")
        print(respuesta)


