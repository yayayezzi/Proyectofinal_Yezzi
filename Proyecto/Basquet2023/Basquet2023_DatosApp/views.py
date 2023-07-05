from django.shortcuts import render, redirect
from Basquet2023_DatosApp.forms import RegistroCuentaForm, equipoForm

def inicio(request):
    return render(request, "Basquet2023_DatosApp/index.html")

def usuario(request):
    return render(request, 'Basquet2023_DatosApp/usuario.html')

def registrarcuenta(request):
    if request.method == 'POST':
        form = RegistroCuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirecciona a la página de inicio después del registro exitoso
    else:
        form = RegistroCuentaForm()
    
    return render(request, 'registrarcuenta.html', {'form': form})

def equipo(request):
    if request.method == 'POST':
        form = equipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos')  # Redirecciona a la página de equipos después de guardar
    else:
        form = equipoForm()
    
    return render(request, 'equipos.html', {'form': form})