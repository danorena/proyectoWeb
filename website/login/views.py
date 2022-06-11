from django.shortcuts import render

# Create your views here.
def callLogin(request):
    return render(request,'login.html')
    # return None