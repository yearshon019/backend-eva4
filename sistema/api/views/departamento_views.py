from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly
from api.response_mixin import StandardResponseMixin

from departamentos.models import Departamento
from api.serializers import DepartamentoSerializer

class DepartamentoViewSet(StandardResponseMixin, ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [IsAdminOrReadOnly]

    success_messages = {
        **StandardResponseMixin.success_messages,
        "create": "Departamento creado correctamente.",
        "update": "Departamento actualizado correctamente.",
        "destroy": "Departamento eliminado correctamente.",
    }
