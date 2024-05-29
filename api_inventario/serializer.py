from rest_framework import serializers
from .models import Inventario


class InventarioSerializer(serializers.ModelSerializer):
    class meta:
        model= Inventario
        fields='__all__'