from django.db import models
from tabnanny import verbose
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):

    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/',blank=True,null=True)

class Acerca_de(models.Model):
    nombre = models.CharField(max_length=30)

class Vuelo(models.Model):

    id_vuelo = models.IntegerField()
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    ida = models.DateTimeField()
    vuelta = models.DateTimeField()
    precio = models.DecimalField(max_digits=8,decimal_places=0)
    imagen = models.URLField(blank=True,null=True)

class Hotel(models.Model):

    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=150)
    desde = models.DateTimeField()
    hasta = models.DateTimeField()
    precio = models.DecimalField(max_digits=8,decimal_places=0)
    imagen = models.URLField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "Hoteles"

class Excursion(models.Model):

    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=150)
    duracion = models.IntegerField()
    precio = models.DecimalField(max_digits=8,decimal_places=0)
    imagen = models.URLField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "Excursiones"
    #def __str__(self) -> str:
    #    return f"Excursion:{self.nombre} en {self.ubicacion} con precio {self.precio}"

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursion, related_name="comments",on_delete=models.CASCADE)
    body = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return '%s - %s' %(self.excursion.nombre, self.autor)