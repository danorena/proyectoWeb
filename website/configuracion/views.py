from django.shortcuts import render
from django.contrib import messages
import mysql.connector as sql

# Create your views here.
def configuracionCall(request):
    m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
    cursor = m.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    m.close()
    print(session[0])
    if session[0] == 'True':
        if request.method == 'POST':
            m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
            s = f"CALL `spSearchIdUserS`();"
            cursor = m.cursor()
            cursor.execute(s)
            idUser = cursor.fetchone()
            id = idUser[0]
            m.close()
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
                abrirConexion = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
                cursor = abrirConexion.cursor()
                procUpdateUser = f"CALL spUpdateUser('{id}','{email}', '{user}','{password}');"

                cursor.execute(procUpdateUser)
                abrirConexion.commit()
                messages.success(request,'Usuario editado correctamente')
                abrirConexion.close()
                return render(request,'configuracion.html')
            elif(password != confirm):
                messages.error(request,'Las Contraseñas no coinciden')
                return render(request,'configuracion.html')
        return render(request,'configuracion.html')
    else:
        return render(request,'logearse.html')

    