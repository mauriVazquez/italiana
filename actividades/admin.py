# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Actividad
from django.shortcuts import redirect


def reporte_actividades(modeladmin, request, queryset):
    return redirect('/actividades/reporte_actividades')

reporte_actividades.short_description = "Reporte de actividades"


class ActividadAdmin(admin.ModelAdmin):
    actions = [reporte_actividades]


admin.site.register(Actividad, ActividadAdmin)

