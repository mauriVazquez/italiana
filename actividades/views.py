# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json

from .models import Actividad
from clientes.models import Cliente


def reporte_actividades(request):
    actividades = Actividad.objects.all()
    actividad_cantidad = {}

    for actividad in actividades:
        cant_clientes = Cliente.objects.filter(actividades__nombre=actividad.nombre).count()
        actividad_cantidad[actividad.nombre] = cant_clientes

    context = {
        "actividad_cantidad": json.dumps(actividad_cantidad, ensure_ascii=False),
    }

    return render(request, "actividades/reporte_actividades.html", context)
