from rest_framework import viewsets, status
from rest_framework.response import Response
from usuarios.permissions import SoloAdminPuedeEscribir
from .models import Barrera
from .serializers import BarreraSerializer

class BarreraViewSet(viewsets.ModelViewSet):
    queryset = Barrera.objects.all()
    serializer_class = BarreraSerializer
    permission_classes = [SoloAdminPuedeEscribir]

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Barrera.DoesNotExist:
            return Response({"detail": "Barrera no encontrada."}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
