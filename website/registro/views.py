from django.shortcuts import render
import mysql.connector as sql

user = ''
email = ''
password = ''

 
# Create your views here.
def callRegister(request):
    pass
    global user,email,s,em,pwd 
    if request.method == 'POST':
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
        
    return render(request,'register.html')
            