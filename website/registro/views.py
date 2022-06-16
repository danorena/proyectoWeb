from django.shortcuts import render
from django.contrib import messages
import mysql.connector as sql



 
# Create your views here.
def callRegister(request):
    if request.method == 'POST':
        user = ''
        email = ''
        password = ''
        m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
        cursor = m.cursor()
        d= request.POST
        for key,value in d.items():
            if key=='user':
                user = value
            if key== 'email':
                email = value
            if key == 'password':
                password = value
                
        c = f"CALL `spInsertUser`('{email}', '{user}', '{password}');"
        cursor.execute(c)
        m.commit()
        messages.error(request,'Usuario registrado correctamente')
        return render(request,'register.html')
        
    return render(request,'register.html')
            