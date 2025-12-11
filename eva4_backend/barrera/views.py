from rest_framework import viewsets
from usuarios.permissions import SoloAdminPuedeEscribir
from .models import Barrera
from .serializers import BarreraSerializer

class BarreraViewSet(viewsets.ModelViewSet):
    queryset = Barrera.objects.all()
    serializer_class = BarreraSerializer
    permission_classes = [SoloAdminPuedeEscribir]
