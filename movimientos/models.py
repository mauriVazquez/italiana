# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from actividades.models import Actividad


class FormaPago(models.Model):
    tipo = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.tipo


class Movimiento(models.Model):
    # egreso negativo y ingreso positivo
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    forma_pago = models.ForeignKey(FormaPago)
    actividad = models.ForeignKey(Actividad)

    def __unicode__(self):
        return "%s | $%s" %(self.actividad, self.monto)
