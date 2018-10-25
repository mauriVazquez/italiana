from django.contrib import admin

from .models import Cliente, Telefono

class TelefonoInline(admin.TabularInline):
    model = Telefono
    fields = ("tipo", "valor")
    extra = 1
    

class ClienteAdmin(admin.ModelAdmin):
    fields = ("nombre", "email", "tutor","actividades")
    inlines = [
        TelefonoInline,
    ]


admin.site.register(Telefono)
admin.site.register(Cliente, ClienteAdmin)
