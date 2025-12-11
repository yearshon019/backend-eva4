
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
        uid = request.data.get('uid', '').strip()

        if not uid:
            return Response({"detail": "Debe enviar el campo 'uid'."}, status=400)

        sensor = SensorRFID.objects.filter(uid=uid).select_related("departamento").first()

        # Caso UID inexistente
        if not sensor:
            evento = EventoAcceso.objects.create(
                sensor=None,
                tipo_evento="ACCESO",
                resultado="DENEGADO",
                departamento=None,
                usuario_operador=request.user,
                detalle="UID no registrado en el sistema."
            )
            return Response({
                "uid": uid,
                "resultado": "DENEGADO",
                "detalle": "UID no registrado",
                "evento_id": evento.id
            }, status=404)

        # Sensor existe → interpretar estado
        estado = sensor.estado
        departamento = sensor.departamento

        if estado == "ACTIVO":
            resultado = "PERMITIDO"
            detalle = "Acceso permitido."
        else:
            resultado = "DENEGADO"
            detalle = f"Sensor {estado}. Acceso denegado."

        # Registrar evento
        evento = EventoAcceso.objects.create(
            sensor=sensor,
            tipo_evento="ACCESO",
            resultado=resultado,
            departamento=departamento,
            usuario_operador=request.user,
            detalle=detalle
        )

        # Abrir barrera si permitido
        if resultado == "PERMITIDO":
            try:
                barrera = Barrera.objects.first()
                if barrera:
                    barrera.estado = "ABIERTA"
                    barrera.save()
            except Exception:
                pass  # No interrumpe el acceso

        return Response({
            "uid": uid,
            "resultado": resultado,
            "detalle": detalle,
            "evento_id": evento.id,
            "departamento": departamento.nombre if departamento else None,
        }, status=200)
