from django.shortcuts import render
from django.contrib import messages
from website.conexion import Conexion

# Create your views here.

conn = Conexion('localhost','root','','usuarios')

def configuracionCall(request):
    #Creamos cursor
    db = conn.dbConexion()
    cursor = db.cursor()
    #Llamamos procedimiento para consultar estado de la sesion actual (Si esta activa la sesion)
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    #Almacenamos datos que retorna el procedimiento en variables
    id = session[3]
    userS = session[2]
    db.close()
    print("id actual: ",id)
    #Si la sesion esta activa ejecutaremos el resto de la funcion
    if session[0] == 'True':
        if request.method == 'POST':
            #Creamos cursor
            db = conn.dbConexion()
            cursor = db.cursor()
            #llamando procedimiento almacenado para buscar La id del usuario en la sesion actual
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
                #Creamos cursor
                db = conn.dbConexion()
                cursor = db.cursor()
                #llamando procedimiento almacenado para actulizar los datos del usuario actual
                procUpdateUser = f"CALL spUpdateUser('{id}','{email}', '{user}','{password}');"
                cursor.execute(procUpdateUser)
                db.commit()
                #Mandamos mensaje de satisfactorio
                messages.success(request,'Usuario editado correctamente')
                db.close()
                return render(request,'configuracion.html',{'usuario' : userS})
            elif(password != confirm):
                #Mandamos mensaje de error
                messages.error(request,'Las Contraseñas no coinciden')
                return render(request,'configuracion.html',{'usuario' : userS})
        return render(request,'configuracion.html',{'usuario' : userS})
    else:
        return render(request,'logearse.html')
 
def deleteCall(request):
    #Creamos cursor
    db = conn.dbConexion()
    cursor = db.cursor()
    #llamando procedimiento almacenado para buscar datos de la sesion actual
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    #Almacenamos datos que retorna el procedimiento dentro de variables
    id = session[3]
    userS = session[2]
    db.close() 
    #Si la sesion esta activa realizamos el resto de la funcion
    if session[0] == 'True':
        if request.method == 'POST':
            #Creamos cursor
            db = conn.dbConexion()
            cursor = db.cursor()
            #llamando procedimiento almacenado para eliminar usuario actual
            procDeleteUser = f"CALL spDeleteUser('{id}');"
            cursor.execute(procDeleteUser)
            db.commit()
            #Mandamos mensaje de satisfactorio
            messages.success(request,'Usuario eliminado correctamente')
            db.close()
            db = conn.dbConexion()
            cursor = db.cursor()
            #llamando procedimiento almacenado para cambiar el estado de la sesion al eliminar el usuario actual
            a = "CALL `spUpdateSession`('False');"
            cursor.execute(a)
            db.commit()
            return render(request,'delete.html')
        else:
            return render(request,'delete.html',{'usuario' : userS})
    else:
        return render(request,'logearse.html')