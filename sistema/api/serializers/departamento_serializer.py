from rest_framework import serializers
from departamentos.models import Departamento
from api.serializers.utils import validar_fk

class DepartamentoSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=100,
        error_messages={
            "blank": "El nombre del departamento es obligatorio.",
            "required": "El nombre del departamento es obligatorio."
        }
    )

    descripcion = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "blank": "La descripción del departamento es obligatoria.",
            "required": "La descripción del departamento es obligatoria."
        }
    )

    class Meta:
        model = Departamento
        fields = '__all__'
        extra_kwargs = {
            "nombre": {"validators": []}
        }

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "El nombre debe tener al menos 3 caracteres."
            )

        if Departamento.objects.filter(nombre=value).exists():
            raise serializers.ValidationError(
                "Ya existe un departamento con este nombre."
            )

        return value
