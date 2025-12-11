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
