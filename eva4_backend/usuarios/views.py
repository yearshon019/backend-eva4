from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import PerfilUsuario
from .serializers import UsuarioSerializer, PerfilUsuarioSerializer
from .permissions import SoloAdminPuedeEscribir

User = get_user_model()

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Solo lectura de usuarios (para admin u operador).
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]


class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    """
    CRUD de perfiles (solo ADMIN puede crear/editar/borrar).
    """
    queryset = PerfilUsuario.objects.select_related('user').all()
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [SoloAdminPuedeEscribir]
