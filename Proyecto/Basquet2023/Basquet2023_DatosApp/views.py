
from django import forms
from .models import Jugador
from django.shortcuts import render, redirect
from .forms import JugadorForm

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'edad']




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
    return render(request, 'Basquet2023_DatosApp/index.html')