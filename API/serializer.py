from rest_framework import serializers
from .models import Tipo_Producto,Stock,Producto

class Tipo_ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tipo_Producto
        fields='__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields='__all__'