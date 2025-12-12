from django.db import models

class EstadoBarrera(models.Model):
    id_estado_barrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Barrera(models.Model):
    id_barrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_estado_barrera = models.ForeignKey(EstadoBarrera, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
