import mysql.connector
from mysql.connector import Error
from model.model_db import model_db
import json



class database:

	info = ""
	numberRows = 0
	whost =""
	wuser = ""
	wpasswd = ""
	wdb = ""

	def __init__(self):
		self.info = "Se inicia el proceso"
		self.numberRows = 0

		#self.modelo_db = model_db(db_host ='mysql-38c2c1c5-banco.a.aivencloud.com',db_user = 'avnadmin',db_password = 'AVNS_Z95SOUCgT5Kcadl2O9C',db_name = 'defaultdb',db_port = "23529")
"""
		self.modelo_db = model_db(
			db_host ='127.0.0.1',
			db_user = 'root',
			db_password = 'Delacruz1982-',
			db_name = 'todoventas',
			db_port ="3306")
"""

		self.modelo_db = model_db(
			db_host ='mysql-38c2c1c5-banco.a.aivencloud.com',
			db_user = 'avnadmin',
			db_password = 'AVNS_Z95SOUCgT5Kcadl2O9C',
			db_name = 'defaultdb',
			db_port ="23529")


		#self.whost ='mysql-38c2c1c5-banco.a.aivencloud.com'
		#self.wuser = 'avnadmin'
		#self.wpasswd = 'AVNS_Z95SOUCgT5Kcadl2O9C'
		#self.wdb = 'defaultdb'
		#self.ports = "23529"





	def db_connecion(self):

		try:
			connection = mysql.connector.connect(
				host=self.modelo_db.db_host,
				user=self.modelo_db.db_user,
				passwd=self.modelo_db.db_password,
				db=self.modelo_db.db_name,
				port=self.modelo_db.db_port,
				auth_plugin='mysql_native_password')
			if connection.is_connected():
				return connection
			else:
				return None
		except Error as e:
			print(f"Error al conectarse a MySql -  {e}")
			return None


	def getRows(self,sqlTXT):
		self.coneccion = self.db_connecion()
		if self.coneccion!=None:
			self.cur = self.coneccion.cursor()
			self.cur.execute(sqlTXT)
			self.rows = self.cur.fetchall()
			self.numberRows = self.cur.rowcount
			if self.numberRows==0:
				self.cur.close()
				self.coneccion.close()
				return None
			else:
				self.columns = [col[0] for col in self.cur.description]
				self.data = [dict(zip(self.columns, row)) for row in self.rows]
				self.to_json = json.dumps(self.data, indent=2)
				self.cur.close()
				self.coneccion.close()
				return self.to_json
		else:
			exit()







	def getSimple(self,sqlTXT):
		self.coneccion = self.db_connecion()
		if self.coneccion!=None:
			self.cur = self.coneccion.cursor()
			self.cur.execute(sqlTXT)
			self.rows = self.cur.fetchone()
        
			if self.cur.rowcount==0:
				self.coneccion.close()
				self.cur.close()
				return None
			else:
				self.coneccion.close()
				self.cur.close()            
				return self.rows[0]
		else:
			exit()

    


	def shotSimple(self,sqlTXT):
		self.coneccion = self.db_connecion()
		if self.coneccion!=None:
			self.cur = self.coneccion.cursor()
			try:
				self.cur.execute(sqlTXT)
			except Error as e:
				self.coneccion.close()
				self.cur.close()
				exit()
				return -1
				


			self.coneccion.commit()

			if self.cur.rowcount==0:
				self.coneccion.close()
				self.cur.close()
				return None
			else:
				self.coneccion.close()
				self.cur.close()            
				return 1
		else:
			exit()









"""
db = dataBase()
datos = db.getRows("select clave,nombre from clientes where clave=62864")
if datos!=None:
	info = json.loads(datos)
	print(info[0]["clave"])
	print(info[0]["nombre"])	



datos = db.getSimple("select grupo4 from clientes where clave=62864")
print(datos)


datos = db.shotSimple("update sj_ctrl_fact_electronica set sj_estado=0")
print(datos)
"""