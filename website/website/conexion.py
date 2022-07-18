class Conexion:
    def __init__(self,host,user,pw,db) -> None:
        self.host = host
        self.user = user
        self.pw = pw
        self.db = db
    
    def dbConexion(self):
        import mysql.connector as sql
        try:
            conectado = sql.connect(host=self.host,user=self.user,passwd=self.pw,database=self.db)
            return conectado
        except:
            print ('Error al conectar a la db')
