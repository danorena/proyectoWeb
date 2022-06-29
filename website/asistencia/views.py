from django.shortcuts import render


# Create your views here.
def asistenciaCall(request):
    fichas = dir()
    return render(request,'asistencia.html',{'fichas' : fichas})

# Hacemos una funcion para leer las fichas
def dir():
    import os
    # buscamos la ruta que contiene todas la fichas
    path  = 'C:\\Users\David\Desktop\proyectoWeb\\fichas'
    # guardamos todas las fichas en una lista iterable
    grupo = os.listdir(path)
    # Devolvemos una lista para iterar sobre esta 
    return grupo

