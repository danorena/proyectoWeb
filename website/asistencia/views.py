from django.shortcuts import render
from website.conexion import Conexion


# Create your views here.

conn = Conexion('localhost',
                'root',
                '',
                'usuarios')

# Create your views here.
def asistenciaCall(request):
    #Creamos cursor
    db = conn.dbConexion()
    cursor = db.cursor()
    #llamando procedimiento almacenado para obtener datos de la sesion actual
    a = f"CALL `spSession`();"
    cursor.execute(a)
    session = cursor.fetchone()
    #Si la sesion esta activa realizamos el resto de la funcion
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
            try:
                asistencia = Asistencia(ficha,date)
                asistencia.toHtml(asistencia.dataFrameAsistencia(ficha))
                return render(request,'asistenciaFicha.html')
            except:
                return render(request,'error.html')
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