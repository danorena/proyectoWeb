from django.shortcuts import render

# Create your views here.
def asistenciaCall(request):
    return render(request,'asistencia.html')