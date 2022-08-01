from operator import index
from django.shortcuts import render
from website.conexion import Conexion


# Create your views here.

conn = Conexion('butflnhy81ngycrrgvxy-mysql.services.clever-cloud.com',
                'uz5rb8lslbk7ttlx',
                'SR0qUqa17VrBy7FjB2S0',
                'butflnhy81ngycrrgvxy')

def indexCall(request):
    #Creamos cursor
    db = conn.dbConexion()
    cursor = db.cursor()
    #llamando procedimiento almacenado para obtener datos de la sesion actual
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    #Si la sesion esta activa realizamos el resto de la funcion
    if session[0] == 'True':
        return render(request,'index.html')
    else:
        return render(request,'logearse.html')
