from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    inventory = serializers.IntegerField()