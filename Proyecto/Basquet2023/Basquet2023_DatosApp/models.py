from django.db import models

class Liga(models.Model):
    nombre = models.CharField(max_length=100)
    equipos = models.ManyToManyField('Equipo')

    def __str__(self):
        return self.nombre

    def cantidad_equipos(self):
        return self.equipos.count()

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='escudos/')

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    posicion = models.CharField(max_length=50)
    valor_mercado = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_jugadores/')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"