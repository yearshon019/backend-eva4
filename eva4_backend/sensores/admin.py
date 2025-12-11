from django.contrib import admin
from .models import SensorRFID

@admin.register(SensorRFID)
class SensorRFIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'alias', 'estado', 'departamento', 'propietario')
    list_filter = ('estado', 'departamento')
    search_fields = ('uid', 'alias')
