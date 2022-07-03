from django.shortcuts import render

# Create your views here.
def configuracionCall(request):
    return render(request,'configuracion.html')