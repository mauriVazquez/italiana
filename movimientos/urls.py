from django.conf.urls import url

from .views import caja, get_caja, imprimir_recibo, ReciboCreate, generar_caja

urlpatterns = [
    url(r'^caja/', caja),
    url(r'^get_caja/', get_caja),

    url(r'^recibo/add/(?P<pk>[0-9]+)', ReciboCreate.as_view(), name='recibo-add'),
    # url(r'^cobro/(?P<pk>[0-9]+)', generar_recibo),

    url(r'^imprimir_recibo/(?P<pk>[0-9]+)', imprimir_recibo),
]
