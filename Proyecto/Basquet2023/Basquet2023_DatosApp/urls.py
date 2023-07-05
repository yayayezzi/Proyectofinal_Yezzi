from django.urls import path
from Basquet2023_DatosApp import views


urlpatterns = [  
    path('inicio/', views.inicio, name='inicio'),
    path('usuario/' , views.usuario, name='usuario'),
    path('equipos/' , views.equipo, name='equipos'),
    path('registrarcuenta/', views.registrarcuenta, name='registrarcuenta'),
     ]



