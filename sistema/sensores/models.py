from django.db import models
from django.core.validators import MinLengthValidator
class EstadoSensor(models.Model):
    id_estado_sensor = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_estado

class SensorRFID(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(4)])
    alias = models.CharField(max_length=100)
    id_estado_sensor = models.ForeignKey(EstadoSensor, on_delete=models.CASCADE)
    id_departamento = models.ForeignKey('departamentos.Departamento', on_delete=models.CASCADE)

    def __str__(self):
        return self.uid
