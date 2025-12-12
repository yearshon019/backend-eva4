from django.db import models
from django.utils import timezone

class EventoAcceso(models.Model):
    id_evento = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField(default=timezone.now)
    uid_leido = models.CharField(max_length=100)
    resultado = models.CharField(max_length=50)
    detalle = models.TextField()
    id_sensor = models.ForeignKey('sensores.SensorRFID', on_delete=models.CASCADE)
    id_departamento = models.ForeignKey('departamentos.Departamento', on_delete=models.CASCADE)
    id_barrera = models.ForeignKey('barreras.Barrera', on_delete=models.CASCADE)

    def __str__(self):
        return f"Evento {self.id_evento} - {self.resultado}"
