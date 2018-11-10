# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import admin

from models import Actividad
from clientes.models import Cliente
from movimientos.models import Recibo


def reporte_actividades(request):
    context = {
        "title": "Reporte de actividades",
    }
    context.update(admin.site.each_context(request))

    return render(request, "actividades/reporte_actividades.html", context)


def get_clientes_x_actividad(request):
    actividades = Actividad.objects.all()
    actividad_cantidad = {}

    for actividad in actividades:
        cant_clientes = Cliente.objects.filter(actividades__nombre=actividad.nombre).count()
        actividad_cantidad[actividad.nombre] = cant_clientes

    return JsonResponse(actividad_cantidad)


def get_deudores(request, pk):
    actividad = Actividad.objects.get(pk=pk)

    # obtengo recibos del ultimo mes
    hoy = datetime.today()
    recibos_mes_actual = Recibo.objects.filter(fecha__month=hoy.month, actividad__pk=actividad.pk)

    #obtengo clientes anotados a la actividad
    clientes_de_actividad = Cliente.objects.filter(actividades__pk=actividad.pk)

    #creo la lista de deudores y las relleno con los clientes
    #que no aparecen dentro de los recibos del ultimo mes
    deudores = []

    for cliente in clientes_de_actividad:
        if recibos_mes_actual.filter(cliente__pk=cliente.pk).count() == 0:
            ultimo_recibo = Recibo.objects.filter(cliente__pk=cliente.pk).last()
            if ultimo_recibo:
                deudores.append([cliente, ultimo_recibo])

    context = {
        "title": "Deudores",
        "actividad": actividad,
        "deudores": deudores
    }
    context.update(admin.site.each_context(request))

    return render(request, "actividades/deudores.html", context)
