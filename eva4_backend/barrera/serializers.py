from rest_framework import serializers
from .models import Barrera

class BarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrera
        fields = ['id', 'nombre', 'estado', 'fecha_actualizacion']
        read_only_fields = ['fecha_actualizacion']
