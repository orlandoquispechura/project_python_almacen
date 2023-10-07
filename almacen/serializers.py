from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Category
from .models import Product
from .models import Customer


# Custom Api filtrado de productos por categoria
# ejem: http://127.0.0.1:8000/almacen/productos/?category=1
class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "category": ["exact"],
        }


# ModelViewSet Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# ModelViewSet Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        filterset_class = ProductFilter


# ModelViewSet Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
