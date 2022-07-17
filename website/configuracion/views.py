from django.shortcuts import render
from django.contrib import messages
from website.conexion import Conexion


# Create your views here.

conn = Conexion('localhost','root','','usuarios')
def configuracionCall(request):
    db = conn.dbConexion()
    cursor = db.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    db.close()
    print(session[0])
    if session[0] == 'True':
        if request.method == 'POST':
            db = conn.dbConexion()
            cursor = db.cursor()
            s = f"CALL `spSearchIdUserS`();"
            cursor.execute(s)
            idUser = cursor.fetchone()
            id = idUser[0]
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
                return render(request,'configuracion.html')
            elif(password != confirm):
                messages.error(request,'Las Contraseñas no coinciden')
                return render(request,'configuracion.html')
        return render(request,'configuracion.html')
    else:
        return render(request,'logearse.html')

    