# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.shortcuts import render

from .models import Recibo, CierreCaja

def generar_caja():

    caja = CierreCaja()
    ultimo_cierre = CierreCaja.objects.all().last()

    recibos = Recibo.objects.filter(fecha__gt=ultimo_cierre.fecha)
    #recibos = Recibo.objects.all()
 
    total_efectivo = 0
    total_tarjeta = 0
    for recibo in recibos:
        if recibo.forma_pago.tipo == "Efectivo":
            total_efectivo += recibo.monto
        else:
            total_tarjeta += recibo.monto

    caja.total_efectivo = total_efectivo
    caja.total_tarjeta = total_tarjeta

    caja.save()