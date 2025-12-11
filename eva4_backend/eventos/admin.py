from django.contrib import admin
from .models import EventoAcceso

@admin.register(EventoAcceso)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_evento', 'resultado', 'sensor', 'departamento', 'fecha_hora')
    list_filter = ('tipo_evento', 'resultado')
    search_fields = ('sensor__uid',)
