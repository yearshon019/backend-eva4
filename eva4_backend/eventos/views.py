from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import EventoAcceso
from .serializers import EventoAccesoSerializer

class EventoAccesoViewSet(viewsets.ModelViewSet):
    """
    Eventos de acceso. Puedes dejarlos CRUD completo
    o solo lectura y que se creen desde el endpoint de sensores.
    """
    queryset = EventoAcceso.objects.select_related('sensor', 'departamento', 'usuario_operador').all()
    serializer_class = EventoAccesoSerializer
    permission_classes = [IsAuthenticated]
