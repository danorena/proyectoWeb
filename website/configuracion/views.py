from django.shortcuts import render
from django.contrib import messages
import mysql.connector as sql

# Create your views here.
def configuracionCall(request):

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
                a = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
                u = f"CALL `spUpdateUser`('{id}','{email}', '{user}','{password}');"
                cursor = a.cursor()
                cursor.execute(u)
                valid = a.commit()
                a.close()
                messages.success(request,'Usuario actualizado correctamente')
                return render(request,'configuracion.html')
            elif(password != confirm):
                messages.error(request,'Las Contraseñas no coinciden')
            return render(request,'configuracion.html')
        
        # if valid == ():
        #     messages.error(request,'Error al actualizar')
        #     return render(request,'configuracion.html')
        # else:
        #     messages.success(request,'Actualizado Correctamente')
        #     return render(request,'configuracion.html')
        
    return render(request,'configuracion.html')