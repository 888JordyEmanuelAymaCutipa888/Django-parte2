from django.db import models

# Create your models here.
class DestinoTuristico(models.Model):
    nombreCiudad = models.CharField(max_length = 100)
    descripcionCiudad = models.CharField(max_length = 100)
    precioTour = models.IntegerField()#(max_digits=3)
    ofertaTour = models.BooleanField()
    oferta1 = models.BooleanField(null = True)
    oferta2 = models.BooleanField(default = True)
    oferta1 = models.TextField(blank = True)
