# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.shortcuts import redirect
from django.conf.urls import url

from .models import Recibo, FormaPago, CierreCaja
from .views import generar_caja


class ReciboAdmin(admin.ModelAdmin):
    fields = ('num_recibo', 'forma_pago', 'cliente', 'actividad')
    list_display = ["num_recibo", "cliente", "fecha", "monto"]
    list_display_links = None
    change_list_template = "movimientos/recibo_changelist.html"
    actions = None
    save_as_continue = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/movimientos/imprimir_recibo')

    def response_change(self, request, obj):
        return redirect('/movimientos/imprimir_recibo/%s' % (str(obj.pk)))


class CierreCajaAdmin(admin.ModelAdmin):
    list_display = ["fecha", "recibo_desde", "recibo_hasta", "total_efectivo", "total_tarjeta", "total"]
    change_list_template = "movimientos/caja_changelist.html"
    list_display_links = None
    actions = None

    def total(self, obj):
        return obj.total_efectivo + obj.total_tarjeta

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        urls = super(CierreCajaAdmin, self).get_urls()
        my_urls = [
            url(r'^generar_caja/', generar_caja),
        ]
        return my_urls + urls


admin.site.register(Recibo, ReciboAdmin)
admin.site.register(FormaPago)
admin.site.register(CierreCaja, CierreCajaAdmin)
