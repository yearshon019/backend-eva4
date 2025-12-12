from rest_framework import serializers
from barreras.models import Barrera
from api.serializers.utils import validar_fk

class BarreraSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=100,
        error_messages={
            "blank": "El nombre de la barrera es obligatorio.",
            "required": "El nombre de la barrera es obligatorio."
        }
    )

    ubicacion = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "blank": "La ubicación de la barrera es obligatoria.",
            "required": "La ubicación de la barrera es obligatoria."
        }
    )

    class Meta:
        model = Barrera
        fields = '__all__'

    def validate(self, data):
        validar_fk(data.get("id_estado_barrera"), "estado de la barrera")
        return data
