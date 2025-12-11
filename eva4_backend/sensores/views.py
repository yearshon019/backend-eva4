from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from usuarios.permissions import SoloAdminPuedeEscribir
from .models import SensorRFID
from .serializers import SensorRFIDSerializer

from eventos.models import EventoAcceso
from barrera.models import Barrera

class SensorRFIDViewSet(viewsets.ModelViewSet):
    queryset = SensorRFID.objects.select_related('departamento', 'propietario').all()
    serializer_class = SensorRFIDSerializer
    permission_classes = [SoloAdminPuedeEscribir]

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated], url_path='validar')
    def validar_acceso(self, request):
        """
        Endpoint para simular la lectura de un RFID.
        Recibe JSON: {"uid": "ABCD1234"}
        Crea un EventoAcceso y responde PERMITIDO o DENEGADO.
        """
        uid = request.data.get('uid', '').strip()

        if not uid:
            return Response(
                {"detail": "Debe enviar el campo 'uid'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        sensor = SensorRFID.objects.filter(uid=uid).select_related('departamento').first()

        if sensor is None:
            # No existe → acceso denegado
            resultado = 'DENEGADO'
            detalle = 'UID no registrado en el sistema.'
            departamento = None
        else:
            departamento = sensor.departamento
            if sensor.estado == 'ACTIVO':
                resultado = 'PERMITIDO'
                detalle = 'Acceso permitido. Sensor en estado ACTIVO.'
            elif sensor.estado == 'INACTIVO':
                resultado = 'DENEGADO'
                detalle = 'Sensor INACTIVO. Acceso denegado.'
            elif sensor.estado == 'BLOQUEADO':
                resultado = 'DENEGADO'
                detalle = 'Sensor BLOQUEADO. Acceso denegado.'
            else:  # PERDIDO u otro
                resultado = 'DENEGADO'
                detalle = 'Sensor marcado como PERDIDO. Acceso denegado.'

        # Registrar evento
        evento = EventoAcceso.objects.create(
            sensor=sensor if sensor else None,
            tipo_evento='ACCESO',
            resultado=resultado,
            departamento=departamento,
            usuario_operador=request.user,
            detalle=detalle,
        )

        # (Opcional) abrir barrera si permitido
        if resultado == 'PERMITIDO':
            barrera = Barrera.objects.first()
            if barrera:
                barrera.estado = 'ABIERTA'
                barrera.save()

        return Response({
            "uid": uid,
            "resultado": resultado,
            "detalle": detalle,
            "evento_id": evento.id,
            "departamento": departamento.nombre if departamento else None,
        }, status=status.HTTP_200_OK)
