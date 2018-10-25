from django.conf.urls import url

from .views import caja, get_caja, imprimir_recibo

urlpatterns = [
    url(r'^caja/', caja),
    url(r'^get_caja/', get_caja),
    url(r'^imprimir_recibo/(?P<pk>[0-9]+)', imprimir_recibo),
]
