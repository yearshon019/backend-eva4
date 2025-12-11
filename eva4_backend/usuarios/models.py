from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PerfilUsuario(models.Model):
    ROL_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('OPERADOR', 'Operador'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='OPERADOR')

    def __str__(self):
        return f"{self.user.username} ({self.rol})"
