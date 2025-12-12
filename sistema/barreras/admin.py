from django.contrib import admin
from .models import Barrera, EstadoBarrera

@admin.register(EstadoBarrera)
class EstadoBarreraAdmin(admin.ModelAdmin):
    list_display = ('id_estado_barrera', 'nombre')

@admin.register(Barrera)
class BarreraAdmin(admin.ModelAdmin):
    list_display = ('id_barrera', 'nombre', 'id_estado_barrera', 'ubicacion')
