from django.db import models

# Create your models here.


class Vuelo(models.Model):

    id_vuelo = models.IntegerField()
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    ida = models.DateTimeField()
    vuelta = models.DateTimeField()
    precio = models.DecimalField(max_digits=8,decimal_places=0)

class Hotel(models.Model):

    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=150)
    desde = models.DateTimeField()
    hasta = models.DateTimeField()
    precio = models.DecimalField(max_digits=8,decimal_places=0)

class Excursion(models.Model):

    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=150)
    duracion = models.IntegerField()
    precio = models.DecimalField(max_digits=8,decimal_places=0)