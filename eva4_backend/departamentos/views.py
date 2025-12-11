from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import SoloAdminPuedeEscribir
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [SoloAdminPuedeEscribir]
