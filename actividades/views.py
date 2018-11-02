# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import admin

from .models import Actividad
from clientes.models import Cliente


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
