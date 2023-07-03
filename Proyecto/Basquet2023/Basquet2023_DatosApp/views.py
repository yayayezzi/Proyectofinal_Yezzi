

from .models import Jugador
from django.shortcuts import render, redirect
from Basquet2023_DatosApp.forms import JugadorForm
from django.contrib.auth.decorators import login_required



def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista')  # Redirecciona a una vista después de guardar el jugador
    else:
        form = JugadorForm()
    
    return render(request, 'Basquet2023_DatosApp/crear_jugador.html')


def inicio(request):
    return render(request, "Basquet2023_DatosApp/index.html")

@login_required
def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            jugador = form.save(commit=False)
            jugador.equipo = request.user.equipo  # Asigna el equipo del usuario actual
            jugador.save()
            return redirect('inicio')  # Redirecciona a la página de inicio
    else:
        form = JugadorForm()
    
    return render(request, 'agregar_jugador.html', {'form': form})