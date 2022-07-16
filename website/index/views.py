from operator import index
from django.shortcuts import render
import mysql.connector as sql

# Create your views here.
# def indexCall(request):
#     from login.views import session
#     if session == True:
#         return render(request,'index.html')
#     else:
#         return render(request,'logearse.html')

def indexCall(request):
    m = sql.connect(host='localhost',user='root',passwd='',database='usuarios')
    cursor = m.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    print (session[0])
    if session[0] == 'True':
        return render(request,'index.html')
    else:
        return render(request,'logearse.html')
    # return render(request,'index.html')
