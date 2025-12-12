from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api.jwt_views import CustomTokenObtainPairView
from api.views import (
    DepartamentoViewSet,
    SensorViewSet,
    BarreraViewSet,
    EventoViewSet,
    api_info
)

# Router REST
router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'sensores', SensorViewSet, basename='sensores')
router.register(r'barreras', BarreraViewSet, basename='barreras')
router.register(r'eventos', EventoViewSet, basename='eventos')

urlpatterns = [
    # 🔐 Autenticación JWT (PERSONALIZADA)
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ℹ️ Endpoint público obligatorio
    path('info/', api_info, name='api-info'),

    # 📦 Endpoints REST
    path('', include(router.urls)),
]
