from django.contrib import admin

from .models import Cliente, Telefono
import adminactions.actions as action
from adminactions.signals import adminaction_requested

class TelefonoInline(admin.TabularInline):
    model = Telefono
    fields = ("tipo", "valor")
    extra = 1
    

class ClienteAdmin(admin.ModelAdmin):
    fields = ("nombre", "email", "tutor", "actividades")
    inlines = [
        TelefonoInline,
    ]


admin.site.register(Telefono)
admin.site.register(Cliente, ClienteAdmin)

# register all adminactions
admin.site.add_action(action.graph_queryset)
#action.add_to_site(admin.site)

def myhandler(sender, action, request, queryset, modeladmin, form, **kwargs):
    assert False, queryset.actividades

adminaction_requested.connect(myhandler, sender=ClienteAdmin)
