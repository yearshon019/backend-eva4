from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def api_info(request):
    return Response({
        "autor": ["TU NOMBRE"],
        "asignatura": "Programación Back End",
        "proyecto": "SmartConnect API",
        "descripcion": "API RESTful para control de accesos RFID con autenticación JWT.",
        "version": "1.0"
    })
