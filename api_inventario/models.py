from django.db import models


class Inventario(models.Model):
    nombre = models.CharField(max_length=250, verbose_name='Nombre')
    cantidad = models.CharField(max_length=150, verbose_name='Cantidad')
    precio = models.CharField(max_length=150, verbose_name='Costo')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventario'
    
    def __str__(self):
        return self.nombre
