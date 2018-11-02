# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.contrib import admin

from clientes.models import Cliente
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


class ReciboCreate(CreateView):
    model = Recibo
    fields = ["forma_pago"]

    def get_context_data(self, **kwargs):
        context = super(ReciboCreate, self).get_context_data(**kwargs)
        client_id = self.kwargs["pk"]
        cliente = Cliente.objects.get(pk=client_id)
        context["title"] = "Recibo"
        context["actividades"] = self.get_actividades(cliente)
        context["cliente"] = cliente
        context.update(admin.site.each_context(self.request))
        return context

    def get_actividades(self, cliente):
        actividades = cliente.actividades.all()
        return actividades

    def form_valid(self, form):
        actividades = self.request.POST.getlist("actividades[]", None)
        cliente_id = self.request.POST.get("cliente")
        monto = self.request.POST.get("monto")
        forma_pago_id = self.request.POST.get("forma_pago")
        num_recibo = Recibo.objects.all().latest('num_recibo').num_recibo + 1

        recibo = Recibo()
        recibo.num_recibo = num_recibo
        recibo.monto = monto
        recibo.cliente_id = cliente_id
        recibo.forma_pago_id = forma_pago_id
        recibo.save()

        if actividades:
            actividades = actividades[0].split(",")

            for actividad in actividades:
                recibo.actividad.add(actividad)

        # instance = form.save(commit=True)

        # return super(ReciboCreate, self).form_valid(form)
        return redirect('/movimientos/imprimir_recibo/%s' % (str(recibo.pk)))


def imprimir_recibo(request, pk):
    recibo = Recibo.objects.get(pk=pk)
    context = {
        "recibo": recibo,
    }

    return render(request, "movimientos/imprimir_recibo.html", context)
