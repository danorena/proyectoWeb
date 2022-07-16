import mysql.connector as sql

class Conexion:
    
    def conectando(self):
        try:
            conectado = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
            print('conectando')
            return conectado
        except:
            print('No conecto')

    def cursor(self,conectado):
        conectado = self.conectando()
        cursor = conectado.cursor()
        return cursor