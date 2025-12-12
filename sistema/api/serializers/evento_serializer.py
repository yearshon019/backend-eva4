from rest_framework import serializers
from eventos.models import EventoAcceso
from api.serializers.utils import validar_fk

class EventoAccesoSerializer(serializers.ModelSerializer):

    uid_leido = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "blank": "El UID leído es obligatorio.",
            "required": "El UID leído es obligatorio."
        }
    )

    resultado = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "blank": "El resultado del evento es obligatorio.",
            "required": "El resultado del evento es obligatorio."
        }
    )

    class Meta:
        model = EventoAcceso
        fields = '__all__'
        read_only_fields = ['fecha_hora']

    def validate_resultado(self, value):
        permitidos = ["PERMITIDO", "DENEGADO"]
        if value.upper() not in permitidos:
            raise serializers.ValidationError(
                "El resultado debe ser PERMITIDO o DENEGADO."
            )
        return value.upper()

    def validate(self, data):
        validar_fk(data.get("id_sensor"), "sensor")
        validar_fk(data.get("id_barrera"), "barrera")
        validar_fk(data.get("id_departamento"), "departamento")
        return data
