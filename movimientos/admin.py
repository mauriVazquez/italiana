# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.shortcuts import redirect

from .models import Recibo, FormaPago, CierreCaja


class ReciboAdmin(admin.ModelAdmin):
    fields = ('num_recibo', 'forma_pago', 'cliente', 'actividad')

    def save_model(self, request, obj, form, change):
        montoTotal = 0
        for actividad in obj.actividad.all():
            montoTotal = montoTotal + actividad.precio
        obj.monto = montoTotal

        #obj.num_recibo = Recibo.objects.all().latest('num_recibo').num_recibo + 1
        super(ReciboAdmin, self).save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/movimientos/imprimir_recibo')

    def response_change(self, request, obj):
        return redirect('/movimientos/imprimir_recibo/%s' % (str(obj.pk)))


admin.site.register(Recibo, ReciboAdmin)
admin.site.register(FormaPago)
admin.site.register(CierreCaja)
