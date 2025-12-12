from rest_framework import serializers
from sensores.models import SensorRFID
from api.serializers.utils import validar_fk

class SensorRFIDSerializer(serializers.ModelSerializer):

    uid = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=100,
        error_messages={
            "blank": "El UID es obligatorio.",
            "required": "El UID es obligatorio."
        }
    )

    class Meta:
        model = SensorRFID
        fields = '__all__'
        extra_kwargs = {
            # Desactiva validadores automáticos
            "uid": {"validators": []}
        }

    def validate_uid(self, value):
        if len(value) < 4:
            raise serializers.ValidationError(
                "El UID debe tener al menos 4 caracteres."
            )

        if SensorRFID.objects.filter(uid=value).exists():
            raise serializers.ValidationError(
                "Ya existe un sensor RFID registrado con este UID."
            )

        return value

    def validate(self, data):
        validar_fk(data.get("id_estado_sensor"), "estado del sensor")
        validar_fk(data.get("id_departamento"), "departamento")
        return data
