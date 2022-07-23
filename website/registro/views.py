from django.shortcuts import render
from django.contrib import messages
from website.conexion import Conexion
from login.views import callLogin


# Create your views here.

conn = Conexion('localhost','root','','usuarios')
def callRegister(request):
    #Creamos cursor
    db = conn.dbConexion()
    cursor = db.cursor()
    #llamando procedimiento almacenado para obtener datos de la sesion actual
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    db.close()
    #Si el usuario de la sesion es administrador realizamos el resto de la funcion
    if session[1] == 2:
        #Si la sesion esta activa realizamos el resto de la funcion
        if session[0] == 'True':
            if request.method == 'POST':
                user = ''
                email = ''
                password = ''
                confirm = ''
                #Creamos cursor
                db = conn.dbConexion()
                cursor = db.cursor()
                d= request.POST
                for key,value in d.items():
                    #Obtenemos user
                    if key=='user':
                        user = value
                    #Obtenemos email
                    if key== 'email':
                        email = value
                    #Obtenemos password
                    if key == 'password':
                        password = value
                    #Obtenemos confirmar password
                    if key == 'confirm':
                        confirm = value
                    #Obtenemos rol a registrar
                    if key == 'rol':
                        rol = value
                if (password == confirm):
                    #llamando procedimiento almacenado para insertar un nuevo usuario
                    c = f"CALL `spInsertUser`('{email}', '{user}', '{password}', '{rol}');"
                    cursor.execute(c)
                    db.commit()
                    db.close()
                    #Mandamos mensaje de satisfactorio
                    messages.success(request,'Usuario registrado correctamente')
                    return render(request,'register.html')
                elif(password != confirm):
                    #Mandamos mensaje de error
                    messages.error(request,'Las Contraseñas no coinciden')
                    return render(request,'register.html')
            return render(request,'register.html')
        else:
            return render(request,'logearse.html')
    else:
        return render(request,'indexA.html')