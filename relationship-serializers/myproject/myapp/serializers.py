from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal

from .models import Category

# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     price = serializers.DecimalField(max_digits=5, decimal_places=2)
#     inventory = serializers.IntegerField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'price_with_tax', 'stock', 'category']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)