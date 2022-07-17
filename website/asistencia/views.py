from django.shortcuts import render
from website.conexion import Conexion


# Create your views here.

conn = Conexion('localhost','root','','usuarios')

# Create your views here.
def asistenciaCall(request):
    db = conn.dbConexion()
    cursor = db.cursor()
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    print (session[0])
    if session[0] == 'True':
        from .Asistencia import Asistencia
        if request.method == 'POST':
            d= request.POST
            for key,value in d.items():
                # Obtiene la fecha 
                if key=='date':
                    date = value
                # Obtiene ficha
                if key == 'ficha':
                    ficha = value
            # fecha = '2022-05-11'
            # ficha = '01'
            asistencia = Asistencia(ficha,date)
            asistencia.toHtml(asistencia.dataFrameAsistencia(ficha))
            return render(request,'asistenciaFicha.html')
        fichas = dir()
        return render(request,'asistencia.html',{'fichas' : fichas})
    else:
        return render(request,'logearse.html')
    

# Hacemos una funcion para leer las fichas
def dir():
    import os
    from .ruta import ruta
    # buscamos la ruta que contiene todas la fichas
    path  = ruta() 
    # guardamos todas las fichas en una lista iterable
    grupo = os.listdir(path)
    # Devolvemos una lista para iterar sobre esta 
    return grupo