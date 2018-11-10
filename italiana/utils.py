# -*- coding: utf-8 -*-

from django.shortcuts import redirect


def redireccionar(request):
    return redirect('/admin')
