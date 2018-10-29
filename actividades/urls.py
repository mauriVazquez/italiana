from django.conf.urls import url

from .views import reporte_actividades

urlpatterns = [
    url(r'^reporte_actividades/', reporte_actividades),
]
