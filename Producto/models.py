from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()


class Material(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad_comprada_gramos = models.DecimalField(
        max_digits=10, decimal_places=0)
    costo_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class DetalleMaterial(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad_utilizada_gramos = models.DecimalField(
        max_digits=7, decimal_places=2)
