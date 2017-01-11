from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=32)

class Carta(models.Model):
    proveedeor= models.ForeignKey(Proveedor)
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()

