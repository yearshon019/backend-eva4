from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import EventoAcceso
from .serializers import EventoAccesoSerializer

class EventoAccesoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventoAcceso.objects.select_related('sensor', 'departamento', 'usuario_operador').all()
    serializer_class = EventoAccesoSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": "Error interno"}, status=500)
