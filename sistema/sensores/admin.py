from django.contrib import admin
from .models import SensorRFID, EstadoSensor

@admin.register(EstadoSensor)
class EstadoSensorAdmin(admin.ModelAdmin):
    list_display = ('id_estado_sensor', 'nombre_estado')

@admin.register(SensorRFID)
class SensorRFIDAdmin(admin.ModelAdmin):
    list_display = ('id_sensor', 'uid', 'alias', 'id_estado_sensor', 'id_departamento')
    search_fields = ('uid', 'alias')
    list_filter = ('id_estado_sensor', 'id_departamento')
