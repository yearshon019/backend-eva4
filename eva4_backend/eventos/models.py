from django.db import models
from django.contrib.auth import get_user_model
from sensores.models import SensorRFID
from departamentos.models import Departamento

User = get_user_model()

class EventoAcceso(models.Model):
    TIPO_CHOICES = [
        ('ACCESO', 'Acceso RFID'),
        ('APERTURA_MANUAL', 'Apertura manual'),
        ('CIERRE_MANUAL', 'Cierre manual'),
    ]

    RESULTADO_CHOICES = [
        ('PERMITIDO', 'Permitido'),
        ('DENEGADO', 'Denegado'),
    ]

    sensor = models.ForeignKey(
        SensorRFID,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='eventos'
    )

    tipo_evento = models.CharField(max_length=30, choices=TIPO_CHOICES)
    resultado = models.CharField(max_length=20, choices=RESULTADO_CHOICES)
    
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='eventos'
    )

    usuario_operador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='eventos_registrados'
    )

    detalle = models.TextField(blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_evento} - {self.resultado} ({self.fecha_hora})"
