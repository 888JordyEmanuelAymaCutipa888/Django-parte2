from django.db import models

# Create your models here.
class DestinoTuristico(models.Model):
    nombreCiudad = models.TextField()
    descripcionCiudad = models.CharField(max_length = 100)
    precioTour = models.IntegerField()#(max_digits=3)
    ofertaTour = models.BooleanField()
