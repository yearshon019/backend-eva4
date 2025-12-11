from rest_framework import serializers
from .models import EventoAcceso

class EventoAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoAcceso
        fields = [
            'id',
            'sensor',
            'tipo_evento',
            'resultado',
            'departamento',
            'usuario_operador',
            'detalle',
            'fecha_hora',
        ]
        read_only_fields = ['fecha_hora']
