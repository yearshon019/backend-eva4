from django.contrib import admin
from .models import EventoAcceso

@admin.register(EventoAcceso)
class EventoAccesoAdmin(admin.ModelAdmin):
    list_display = (
        'id_evento',
        'fecha_hora',
        'uid_leido',
        'resultado',
        'id_sensor',
        'id_departamento',
        'id_barrera'
    )
    list_filter = ('resultado', 'fecha_hora')
    search_fields = ('uid_leido',)
