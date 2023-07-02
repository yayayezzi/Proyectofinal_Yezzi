from django.urls import path
from Basquet2023_DatosApp import views
from .views import inicio



urlpatterns = [
    path('crear_jugador/', views.crear_jugador, name='crear_jugador'),
    path('inicio/', inicio, name='inicio'),
    ]



