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

    def validate_tipo_evento(self, value):
        if value not in ["ACCESO", "ERROR"]:
            raise serializers.ValidationError("Tipo de evento no válido.")
        return value
