# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date, datetime, timedelta

from django.shortcuts import render
from django.http import JsonResponse

from .models import Recibo, CierreCaja

def generar_caja():

    caja = CierreCaja()
    ultimo_cierre = CierreCaja.objects.all().last()

    recibos = Recibo.objects.filter(fecha__gt=ultimo_cierre.fecha + timedelta(days=1)).order_by("num_recibo")
    #recibos = Recibo.objects.all().order_by("num_recibo")

    caja.recibo_desde = recibos[0].num_recibo
    caja.recibo_hasta = recibos[len(recibos) - 1].num_recibo

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


def caja(request):

    context = {
        "title": "caja"
    }

    return render(request, 'movimientos/caja.html', context)


def get_caja(request):

    mes = datetime.today().month
    cajas = CierreCaja.objects.filter(fecha__month=mes)

    lista = []
    for caja in cajas:
        dic = {}
        dic['fecha'] = caja.fecha
        dic['recibo_desde'] = caja.recibo_desde
        dic['recibo_hasta'] = caja.recibo_hasta
        dic['total_tarjeta'] = caja.total_tarjeta
        dic['total_efectivo'] = caja.total_efectivo
        lista.append(dic)

    return JsonResponse(lista)


def imprimir_recibo(request, pk):
    recibo = Recibo.objects.get(pk=pk)
    context = {
        "recibo": recibo,
    }
    return render(request, "movimientos/imprimir_recibo.html", context)
