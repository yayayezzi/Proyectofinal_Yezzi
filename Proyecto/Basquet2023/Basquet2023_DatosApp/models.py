from django.db import models

class Cuenta(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    TIPOS_CUENTA = (
        ('periodista', 'Periodista'),
        ('tecnico', 'Técnico'),
        ('jugador', 'Jugador'),
        ('aficionado', 'Aficionado'),
    )
    tipo_cuenta = models.CharField(max_length=50, choices=TIPOS_CUENTA)

    def __str__(self):
        return self.email

class equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre