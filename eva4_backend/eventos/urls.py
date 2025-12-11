from rest_framework.routers import DefaultRouter
from .views import EventoAccesoViewSet

router = DefaultRouter()
router.register(r'', EventoAccesoViewSet, basename='eventoacceso')

urlpatterns = router.urls
