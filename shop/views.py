from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request, 'shop/index.html')
    
def contacto(request) :
    return render(request, 'shop/contacto.html')
  