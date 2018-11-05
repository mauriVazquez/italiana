# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

def directorio_imagen(instance, filename):
    return 'logosActividades/{0}.JPEG'.format(instance.nombre)


class Actividad(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to=directorio_imagen, null=True)

    class Meta():
        verbose_name_plural = "Actividades"

    def __str__(self):
        return self.nombre
