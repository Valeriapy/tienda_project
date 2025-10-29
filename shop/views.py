from django.shortcuts import render, redirect
# from .forms import RemeraForm
from .models import Remera

# --- Vistas principales ---
def index(request):
    remeras = Remera.objects.all()
    return render(request, 'shop/index.html', {'remeras': remeras})

def contacto(request):
    return render(request, 'shop/contacto.html')

# --- Vistas de catálogo ---
""" def nueva_remera(request):
    if request.method == 'POST':
        form = RemeraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RemeraForm()
    return render(request, 'shop/nueva_remera.html', {'form': form})"""
