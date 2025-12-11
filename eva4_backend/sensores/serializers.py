from rest_framework import serializers
from .models import SensorRFID

class SensorRFIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorRFID
        fields = [
            'id',
            'uid',
            'alias',
            'estado',
            'propietario',
            'departamento',
            'fecha_creacion',
            'fecha_actualizacion',
        ]
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']

    def validate_uid(self, value):
        value = value.strip().upper()
        if value == "":
            raise serializers.ValidationError("El UID no puede estar vacío.")
        if len(value) < 4:
            raise serializers.ValidationError("El UID es demasiado corto.")
        if " " in value:
            raise serializers.ValidationError("El UID no puede contener espacios.")
        return value

    def validate_estado(self, value):
        estados_validos = ["ACTIVO", "INACTIVO", "BLOQUEADO", "PERDIDO"]
        if value not in estados_validos:
            raise serializers.ValidationError("Estado no válido.")
        return value
