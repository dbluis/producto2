from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Material(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad_comprada_gramos = models.DecimalField(
        max_digits=10, decimal_places=0)
    costo_total = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class DetalleMaterial(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad_utilizada_gramos = models.DecimalField(
        max_digits=7, decimal_places=2)


class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
