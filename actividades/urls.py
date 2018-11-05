from django.conf.urls import url

from .views import reporte_actividades, get_clientes_x_actividad, get_deudores

urlpatterns = [
    url(r'^reporte_actividades/$', reporte_actividades),
    url(r'^get_clientes_x_actividad/$', get_clientes_x_actividad),
    url(r'^deudores/(?P<pk>[0-9]+)', get_deudores),

]
