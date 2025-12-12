from rest_framework import serializers

def validar_fk(instancia, nombre):
    if not instancia:
        raise serializers.ValidationError(
            f"El {nombre} indicado no existe."
        )
