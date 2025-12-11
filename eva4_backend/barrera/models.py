from django.db import models

class Barrera(models.Model):
    ESTADO_CHOICES = [
        ('ABIERTA', 'Abierta'),
        ('CERRADA', 'Cerrada'),
    ]

    nombre = models.CharField(max_length=100, default="Barrera Principal")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='CERRADA')
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.estado}"
