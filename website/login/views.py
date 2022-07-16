from django.shortcuts import render
from django.contrib import messages
import mysql.connector as sql
from website.conexion import Conexion

# con = Conexion()
# m = con.conectando()

# Create your views here.

def callLogin(request):

    if request.method == 'POST':
        m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
        cursor = m.cursor()
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
            m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
            cursor = m.cursor()
            a = f"CALL `spUpdateSession`('True');"
            cursor.execute(a)
            m.commit()
            return render(request,'index.html', )
    return render(request,'login.html')

def callLogout(request):
    m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
    cursor = m.cursor()
    a = f"CALL `spUpdateSession`('False');"
    cursor.execute(a)
    m.commit()
    return render(request,'logearse.html')