from django.shortcuts import render
from django.contrib import messages
from website.conexion import Conexion

# Create your views here.

conn = Conexion('b60lkhh7i47obofeagt8-mysql.services.clever-cloud.com','uempkk9vesxwg5af','dRzWyHluiDPzEZt68igL','b60lkhh7i47obofeagt8')

def configuracionCall(request):
    db = conn.dbConexion()
    cursor = db.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    id = session[0]
    userS = session[2]
    db.close()
    if session[0] == 'True':
        if request.method == 'POST':
            db = conn.dbConexion()
            cursor = db.cursor()
            s = f"CALL `spSearchIdUserS`();"
            cursor.execute(s)
            idUser = cursor.fetchone()
            db.close()
            d= request.POST
            for key,value in d.items():
                # Recibe usuario
                if key=='txtUser':
                    user = value
                # Recibe pw
                if key=='txtEmail':
                    email = value
                if key == 'txtPass':
                    password = value 
                # Recibe email
                if key == 'confirmPass':
                    confirm = value
            if (password == confirm):
                db = conn.dbConexion()
                cursor = db.cursor()
                procUpdateUser = f"CALL spUpdateUser('{id}','{email}', '{user}','{password}');"
                cursor.execute(procUpdateUser)
                db.commit()
                messages.success(request,'Usuario editado correctamente')
                db.close()
                return render(request,'configuracion.html',{'usuario' : userS})
            elif(password != confirm):
                messages.error(request,'Las Contraseñas no coinciden')
                return render(request,'configuracion.html',{'usuario' : userS})
        return render(request,'configuracion.html',{'usuario' : userS})
    else:
        return render(request,'logearse.html')
 
def deleteCall(request):
    db = conn.dbConexion()
    cursor = db.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    id = session[3]
    userS = session[2]
    db.close() 
    if session[0] == 'True':
        if request.method == 'POST':
            db = conn.dbConexion()
            cursor = db.cursor()
            procDeleteUser = f"CALL spDeleteUser('{id}');"
            cursor.execute(procDeleteUser)
            db.commit()
            messages.success(request,'Usuario eliminado correctamente')
            db.close()
            db = conn.dbConexion()
            cursor = db.cursor()
            a = "CALL `spUpdateSession`('False');"
            cursor.execute(a)
            db.commit()
            return render(request,'delete.html')
        else:
            return render(request,'delete.html',{'usuario' : userS})
    else:
        return render(request,'logearse.html')