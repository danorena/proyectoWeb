from django.shortcuts import render

# Create your views here.
def indexCall(request):
    return render(request,'index.html')