from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly
from api.response_mixin import StandardResponseMixin

from sensores.models import SensorRFID
from api.serializers import SensorRFIDSerializer

class SensorViewSet(StandardResponseMixin, ModelViewSet):
    queryset = SensorRFID.objects.all()
    serializer_class = SensorRFIDSerializer
    permission_classes = [IsAdminOrReadOnly]

    # (opcional) mensaje específico para este recurso
    success_messages = {
        **StandardResponseMixin.success_messages,
        "create": "Sensor RFID creado correctamente.",
        "update": "Sensor RFID actualizado correctamente.",
        "destroy": "Sensor RFID eliminado correctamente.",
    }
