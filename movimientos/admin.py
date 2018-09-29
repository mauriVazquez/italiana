# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Recibo, FormaPago, CierreCaja

admin.site.register(Recibo)
admin.site.register(FormaPago)
admin.site.register(CierreCaja)
