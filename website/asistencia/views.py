from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def asistenciaCall(request):
    return render(request,'asistencia.html')

# Hacemos una funcion para leer las fichas
def dir():
    import os
    # buscamos la ruta que contiene todas la fichas
    path  = 'C:\\Users\\Lucas\\Documents\\Sena\\proyecto-sena\\attendance\\model\\datasets\\attendance_system_dataset'
    # guardamos todas las fichas en una lista iterable
    dir_list = os.listdir(path)
    # Devolvemos una lista para iterar sobre esta 
    return dir_list

# Llamamos la funcion
fichas = dir()

# Iteramos las fichas
for ficha in fichas:
    # Obtenemos cada ficha
    print(ficha)

def python_funct(request):
      #do something with the data passed

      fname=request.GET.get('fname',None)
      lname=request.GET.get('lname',None)
      fullname= fname+' '+lname
      #fullname= 33
      response = {
        'fullname': fullname
         }
      return JsonResponse(response)
