from django.contrib import admin
from django.urls import path, include

# JWT views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    # Rutas de cada app
    path('api/usuarios/', include('usuarios.urls')),
    path('api/departamentos/', include('departamentos.urls')),
    path('api/sensores/', include('sensores.urls')),
    path('api/eventos/', include('eventos.urls')),
    path('api/barrera/', include('barrera.urls')),

    # Endpoint general obligatorio (AHORA SÍ CORRECTO)
    path('api/info/', include('api.urls')),
]
