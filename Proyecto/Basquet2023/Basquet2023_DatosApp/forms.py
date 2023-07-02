from django import forms
from .models import Jugador
from django.shortcuts import render

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'edad']




def buscar_jugador(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        jugadores = Jugador.objects.filter(nombre__icontains=nombre)
        return render(request, 'buscar_jugador.html', {'jugadores': jugadores})
    else:
        return render(request, 'buscar_jugador.html')