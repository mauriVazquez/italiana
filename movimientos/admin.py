# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Movimiento, FormaPago

admin.site.register(Movimiento)
admin.site.register(FormaPago)
