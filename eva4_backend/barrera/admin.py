from django.contrib import admin
from .models import Barrera

@admin.register(Barrera)
class BarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'estado', 'fecha_actualizacion')
