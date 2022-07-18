from django.shortcuts import render
from django.contrib import messages
from website.conexion import Conexion



# Create your views here.

# conn = Conexion('localhost','root','','usuarios')
conn = Conexion('b60lkhh7i47obofeagt8-mysql.services.clever-cloud.com','uempkk9vesxwg5af','dRzWyHluiDPzEZt68igL','b60lkhh7i47obofeagt8')
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
            b = f"CALL `spSearchInfo`('{user}','{password}');"
            cursor.execute(b)
            idUser = cursor.fetchone()
            id = idUser[0]
            rol = idUser[1]
            userS = idUser[2]
            db.close()
            db = conn.dbConexion()
            cursor = db.cursor()
            c = f"CALL `spUpdateInfoSession`('{id}','{rol}','{userS}');"
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