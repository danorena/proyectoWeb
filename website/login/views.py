from django.shortcuts import render
import mysql.connector as sql

user = ''
password = ''

# Create your views here.
def callLogin(request):
    global user,password 
    if request.method == 'POST':
        m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
        cursor = m.cursor()
        d= request.POST
        for key,value in d.items():
            # Valida usuario
            if key=='user':
                user = value
            # Valida pw
            if key == 'password':
                password = value
                
        c = f"CALL `spLogin`('{user}', '{password}');"
        cursor.execute(c)
        m.commit()
        
        valid = tuple(cursor.fetchall())
        if t == ():
            return (request,'login.html')
        else:
            return render(request,'index.html')
            
        
    
 
            