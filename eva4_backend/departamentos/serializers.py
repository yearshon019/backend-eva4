from rest_framework import serializers
from .models import Departamento
import re

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['id', 'nombre', 'descripcion']

    def validate_nombre(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("El nombre del departamento es obligatorio.")

        # No permitir números negativos (ej: "-100")
        if re.search(r"-\d+", value):
            raise serializers.ValidationError("El número del departamento no puede ser negativo.")

        return value

