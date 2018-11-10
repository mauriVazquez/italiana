# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import url, include

from .utils import redireccionar

admin.site.site_header = 'Gestión Asociación Italiana'
admin.site.site_title = 'Gestión Asociación Italiana'
admin.site.site_url = None

urlpatterns = [
    url(r'^$', redireccionar),
    url(r'^admin/', admin.site.urls),
    url(r'^movimientos/', include('movimientos.urls')),
    url(r'^actividades/', include('actividades.urls')),
]
