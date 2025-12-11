from django.db import models
from django.contrib.auth import get_user_model
from departamentos.models import Departamento

User = get_user_model()

class SensorRFID(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
        ('BLOQUEADO', 'Bloqueado'),
        ('PERDIDO', 'Perdido'),
    ]

    uid = models.CharField(max_length=50, unique=True)
    alias = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ACTIVO')
    
    propietario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='sensores'
    )

    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        related_name='sensores'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.uid} ({self.alias or 'Sin alias'})"
