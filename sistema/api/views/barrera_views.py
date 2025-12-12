from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly
from api.response_mixin import StandardResponseMixin

from barreras.models import Barrera
from api.serializers import BarreraSerializer

class BarreraViewSet(StandardResponseMixin, ModelViewSet):
    queryset = Barrera.objects.all()
    serializer_class = BarreraSerializer
    permission_classes = [IsAdminOrReadOnly]

    success_messages = {
        **StandardResponseMixin.success_messages,
        "create": "Barrera creada correctamente.",
        "update": "Barrera actualizada correctamente.",
        "destroy": "Barrera eliminada correctamente.",
    }
