from django.db import models

# Create your models here.
class DestinoTuristico(models.Model):
    nombreCiudad = models.CharField(max_length = 100)
    descripcionCiudad = models.CharField(max_length = 100)
    imagenCiudad = models.ImageField()
    precioTour = models.IntegerField()#(max_digits=3)
    ofertaTour = models.BooleanField()
