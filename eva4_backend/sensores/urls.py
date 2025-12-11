from rest_framework.routers import DefaultRouter
from .views import SensorRFIDViewSet

router = DefaultRouter()
router.register(r'', SensorRFIDViewSet, basename='sensor')

urlpatterns = router.urls
