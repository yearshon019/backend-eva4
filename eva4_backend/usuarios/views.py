from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import PerfilUsuario
from .serializers import UsuarioSerializer, PerfilUsuarioSerializer
from .permissions import SoloAdminPuedeEscribir

User = get_user_model()


class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.select_related('user').all()
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [SoloAdminPuedeEscribir]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
