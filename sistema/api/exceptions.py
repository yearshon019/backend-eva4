from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            "status": response.status_code,
            "error": response.data
        }, status=response.status_code)

    # Error interno no controlado
    return Response({
        "status": 500,
        "error": "Error interno del servidor"
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
