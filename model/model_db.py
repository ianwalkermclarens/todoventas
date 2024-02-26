class model_db():
    def __init__(self,db_host="",db_user="",db_password="",db_name="",db_port=""):
        self.db_host=db_host
        self.db_user=db_user
        self.db_password=db_password
        self.db_name=db_name
        self.db_port=db_port

    def star(self):
        self.db_host ='mysql-38c2c1c5-banco.a.aivencloud.com'
        self.db_user = 'avnadmin'
        self.db_password = 'AVNS_Z95SOUCgT5Kcadl2O9C'
        self.db_name = 'defaultdb'
        self.port = "23529"
