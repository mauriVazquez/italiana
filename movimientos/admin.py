# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.shortcuts import redirect

from .models import Recibo, FormaPago, CierreCaja


class ReciboAdmin(admin.ModelAdmin):
    fields = ('num_recibo', 'forma_pago', 'cliente', 'actividad')
    list_display = ["cliente", "num_recibo", "monto"]

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/movimientos/imprimir_recibo')

    def response_change(self, request, obj):
        return redirect('/movimientos/imprimir_recibo/%s' % (str(obj.pk)))


admin.site.register(Recibo, ReciboAdmin)
admin.site.register(FormaPago)
admin.site.register(CierreCaja)
