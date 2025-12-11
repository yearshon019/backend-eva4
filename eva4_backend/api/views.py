from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def info(request):
    return Response({
        "autor": ["Yearshon Orrego & Kevin Ayala"],
        "asignatura": "Programación Back End",
        "proyecto": "Sistema de Acceso RFID",
        "descripcion": "API REST para control de accesos usando sensores RFID.",
        "version": "1.0"
    })
