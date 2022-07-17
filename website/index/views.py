from operator import index
from django.shortcuts import render
from website.conexion import Conexion


# Create your views here.

conn = Conexion('localhost','root','','usuarios')
def indexCall(request):
    db = conn.dbConexion()
    cursor = db.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    print (session[0])
    if session[0] == 'True':
        
        return render(request,'index.html')
    else:
        return render(request,'logearse.html')
    # return render(request,'index.html')
