class Conexion:
    
    #Constructor para inicializar las variables
    def __init__(self,host,user,pw,db) -> None:
        self.host = host
        self.user = user
        self.pw = pw
        self.db = db
    
    #Creamos funcion para conectarse a la base de datos
    def dbConexion(self):
        import mysql.connector as sql
        try:
            conectado = sql.connect(host=self.host,user=self.user,passwd=self.pw,database=self.db)
            return conectado
        except:
            print ('Error al conectar a la db')
