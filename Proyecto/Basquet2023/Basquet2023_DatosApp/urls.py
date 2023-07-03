from django.urls import path
from Basquet2023_DatosApp import views


urlpatterns = [
    path('crear_jugador/', views.crear_jugador, name='crear_jugador'),
    path('agregar_jugador/', views.crear_jugador, name='agregar_jugador'),
    path('inicio/', views.inicio, name='inicio'),
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('jugadores/', views.listar_jugadores, name='listar_jugadores'),
    path('ligas/', views.listar_ligas, name='listar_ligas'),
    path('usuario/', views.usuario, name='usuario'),
    ]



