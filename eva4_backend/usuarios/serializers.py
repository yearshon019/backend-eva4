from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PerfilUsuario

User = get_user_model()


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = ['id', 'user', 'rol']
