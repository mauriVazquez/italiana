from django.contrib import admin
from django.utils.html import format_html

from .models import Cliente, Telefono


class TelefonoInline(admin.TabularInline):
    model = Telefono
    fields = ("tipo", "valor")
    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    fields = ("nombre", "email", "tutor", "actividades")
    list_display = ["nombre", "cobrar"]
    search_fields = ['nombre']
    inlines = [
        TelefonoInline,
    ]

    def cobrar(self, obj):
        """obj es el cliente"""
        return format_html(
            "<a href='/movimientos/recibo/add/{}'>Cobrar</a>",
            obj.pk,
        )

    cobrar.short_description = "Cobros"


admin.site.register(Cliente, ClienteAdmin)
