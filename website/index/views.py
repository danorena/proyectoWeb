from operator import index
from django.shortcuts import render
from website.conexion import Conexion


# Create your views here.

conn = Conexion('b60lkhh7i47obofeagt8-mysql.services.clever-cloud.com','uempkk9vesxwg5af','dRzWyHluiDPzEZt68igL','b60lkhh7i47obofeagt8')
def indexCall(request):
    db = conn.dbConexion()
    cursor = db.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    if session[0] == 'True':
        
        return render(request,'index.html')
    else:
        return render(request,'logearse.html')
