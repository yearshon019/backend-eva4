from rest_framework import serializers
from .models import Barrera

class BarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrera
        fields = ['id', 'nombre', 'estado', 'fecha_actualizacion']
        read_only_fields = ['fecha_actualizacion']

    def validate_estado(self, value):
        estados_validos = ["ABIERTA", "CERRADA"]
        if value not in estados_validos:
            raise serializers.ValidationError("Estado de barrera no válido.")
        return value
