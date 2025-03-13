from rest_framework import viewsets
from .models import Modulo
from .serializers import ModuloSerializer

class ModuloViewset(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer