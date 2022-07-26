from django.shortcuts import render
from django.contrib import messages
from website.conexion import Conexion



# Create your views here.

conn = Conexion('localhost','root','','b60lkhh7i47obofeagt8')

def callLogin(request):
    if request.method == 'POST':
        #Creamos cursor
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
        #llamando procedimiento almacenado para logearse      
        c = f"CALL `spLogin`('{user}', '{password}');"
        cursor.execute(c)
        
        valid = tuple(cursor.fetchall())
        if valid == ():
            #Generamos mensaje error
            messages.error(request,'Usuario o contrasena incorrectos')
            return render(request,'login.html')
        else:
            #Creamos cursor
            db = conn.dbConexion()
            cursor = db.cursor()
            #llamando procedimiento almacenado para actualizar sesion
            a = "CALL `spUpdateSession`('True');"
            #Creamos cursor
            cursor.execute(a)
            db.commit()
            #llamando procedimiento almacenado para buscar informacion de usuario actual
            b = f"CALL `spSearchInfo`('{user}','{password}');"
            cursor.execute(b)
            idUser = cursor.fetchone()
            #Almacenamos datos que retorna el procedimiento almacenado dentro de variables
            id = idUser[0]
            rol = idUser[1]
            userS = idUser[2]
            db.close()
            #Creamos cursor
            db = conn.dbConexion()
            cursor = db.cursor()
            #llamando procedimiento almacenado para actualizar informacion del usuario en la sesion actual
            c = f"CALL `spUpdateInfoSession`('{id}','{rol}','{userS}');"
            cursor.execute(c)
            db.commit()
            db.close()
            return render(request,'index.html', )
    return render(request,'login.html')

def callLogout(request):
    #Creamos cursor
    db = conn.dbConexion()
    cursor = db.cursor()
    #llamando procedimiento almacenado para cerrar la sesion
    a = "CALL `spUpdateSession`('False');"
    cursor.execute(a)
    db.commit()
    db.close()
    return render(request,'logearse.html')