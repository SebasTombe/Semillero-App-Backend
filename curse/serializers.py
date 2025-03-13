from rest_framework import serializers
from .models import Modulo

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ['id', 'Area', 'NombreModulo', 'DescripcionModulo']
