from django.shortcuts import render
from django.contrib import messages
import mysql.connector as sql
from website.conexion import Conexion


# Create your views here.

conn = Conexion('localhost','root','','usuarios')
def callLogin(request):

    if request.method == 'POST':
        db = conn.dbConexion()
        cursor = db.cursor()
        d= request.POST
        for key,value in d.items():
            # Valida usuario
            if key=='user':
                user = value
            # Valida pw
            if key == 'pass':
                password = value
                
        c = f"CALL `spLogin`('{user}', '{password}');"
        cursor.execute(c)
        
        valid = tuple(cursor.fetchall())
        if valid == ():
            messages.error(request,'Usuario o contrasena incorrectos')
            return render(request,'login.html')
        else:
            db = conn.dbConexion()
            cursor = db.cursor()
            a = "CALL `spUpdateSession`('True');"
            cursor.execute(a)
            db.commit()
            b = f"CALL `spSearchIdRol`('{user}','{password}');"
            cursor.execute(b)
            idUser = cursor.fetchone()
            id = idUser[0]
            rol = idUser[1]
            db.close()
            db = conn.dbConexion()
            cursor = db.cursor()
            c = f"CALL `spUpdateIdRolSession`('{id}','{rol}');"
            cursor.execute(c)
            db.commit()
            db.close()
            return render(request,'index.html', )
    return render(request,'login.html')

def callLogout(request):
    db = conn.dbConexion()
    cursor = db.cursor()
    a = "CALL `spUpdateSession`('False');"
    cursor.execute(a)
    db.commit()
    db.close()
    return render(request,'logearse.html')