from django.shortcuts import render
from django.contrib import messages
import mysql.connector as sql

# Create your views here.
def configuracionCall(request):
    if request.method == 'POST':
        m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
        cursor = m.cursor()
        d= request.POST
        for key,value in d.items():
            # Recibe id
            if key=='idUser':
                idUser = value
            # Recibe usuario
            if key=='txtUser':
                user = value
            # Recibe pw
            if key == 'txtPass':
                password = value 
            # Recibe email
            if key=='txtEmail':
                email = value
                
        c = f"CALL `spUpdateUser`('{idUser}','{email}', '{user}','{password}');"
        cursor.execute(c)
        valid = m.commit()
        if valid == ():
            messages.error(request,'Error al actualizar')
            return render(request,'configuracion.html')
        else:
            messages.success(request,'Actualizado Correctamente')
            return render(request,'configuracion.html')
    return render(request,'configuracion.html')