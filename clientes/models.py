# -*- coding: utf-8 -*-

from django.db import models
from actividades.models import Actividad


class Cliente(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    domicilio = models.CharField(max_length=60, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    tutor = models.ForeignKey("Cliente", null=True, blank=True)
    actividades = models.ManyToManyField(Actividad, blank=True)
    es_socio = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre.encode('utf8')


class Telefono(models.Model):

    TELEFONOS_CHOICES = (
        ("FJ", "Fijo"),
        ("MV", "Celular"),
    )

    tipo = models.CharField(max_length=2, choices=TELEFONOS_CHOICES, default="MV")
    valor = models.CharField(max_length=40)
    cliente = models.ForeignKey(Cliente)

    def __str__(self):
        return '%s - %s' % (self.get_tipo_display(), self.valor)
