from rest_framework import viewsets, status
from rest_framework.response import Response
from usuarios.permissions import SoloAdminPuedeEscribir
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [SoloAdminPuedeEscribir]

    def create(self, request, *args, **kwargs):
        if not request.data.get("nombre"):
            return Response({"detail": "El nombre es obligatorio."}, status=400)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Departamento.DoesNotExist:
            return Response({"detail": "Departamento no encontrado."}, status=404)
