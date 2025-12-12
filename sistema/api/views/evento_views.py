from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly
from api.response_mixin import StandardResponseMixin

from eventos.models import EventoAcceso
from api.serializers import EventoAccesoSerializer

class EventoViewSet(StandardResponseMixin, ModelViewSet):
    queryset = EventoAcceso.objects.all()
    serializer_class = EventoAccesoSerializer
    permission_classes = [IsAdminOrReadOnly]

    success_messages = {
        **StandardResponseMixin.success_messages,
        "create": "Evento de acceso registrado correctamente.",
    }
