from django.shortcuts import render
from django.contrib import messages
from website.conexion import Conexion


# Create your views here.

conn = Conexion('localhost','root','','usuarios')

def callRegister(request):
    db = conn.dbConexion()
    cursor = db.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    db.close()
    print (session[0])
    print (session[1])
    if session[1] == 2:
        if session[0] == 'True':
            if request.method == 'POST':
                user = ''
                email = ''
                password = ''
                confirm = ''
                db = conn.dbConexion()
                cursor = db.cursor()
                d= request.POST
                for key,value in d.items():
                    if key=='user':
                        user = value
                    if key== 'email':
                        email = value
                    if key == 'password':
                        password = value
                    if key == 'confirm':
                        confirm = value
                    if key == 'rol':
                        rol = value
                if (password == confirm):
                    c = f"CALL `spInsertUser`('{email}', '{user}', '{password}', '{rol}');"
                    cursor.execute(c)
                    db.commit()
                    db.close()
                    messages.success(request,'Usuario registrado correctamente')
                    return render(request,'register.html')
                elif(password != confirm):
                    messages.error(request,'Las Contraseñas no coinciden')
                    return render(request,'register.html')
            return render(request,'register.html')
        else:
            return render(request,'logearse.html')
    else:
        return render(request,'index.html')