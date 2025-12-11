from rest_framework.routers import DefaultRouter
from .views import BarreraViewSet

router = DefaultRouter()
router.register(r'', BarreraViewSet, basename='barrera')

urlpatterns = router.urls
