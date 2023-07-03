from django.urls import path
from Basquet2023_DatosApp import views


urlpatterns = [
    path('crear_jugador/', views.crear_jugador, name='crear_jugador'),
    path('agregar_jugador/', views.crear_jugador, name='agregar_jugador'),
    path('inicio/', views.inicio, name='inicio'),
    ]



