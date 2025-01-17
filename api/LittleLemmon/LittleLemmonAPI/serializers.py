from rest_framework import serializers
from .models import MenuItems

class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['id', 'title', 'price', 'inventory']