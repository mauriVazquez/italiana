# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html

from .models import Actividad
from django.shortcuts import redirect


def reporte_actividades(modeladmin, request, queryset):
    return redirect('/actividades/reporte_actividades')

reporte_actividades.short_description = "Reporte de actividades"

class ActividadAdmin(admin.ModelAdmin):
    actions = [reporte_actividades]
    list_display = ["nombre", "deudores"]

    def deudores(self, obj):
        """obj es el cliente"""
        return format_html(
            "<a href='/actividades/deudores/{}'>Deudores</a>",
            obj.pk,
        )


admin.site.register(Actividad, ActividadAdmin)
