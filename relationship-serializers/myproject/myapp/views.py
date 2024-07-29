from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.

@api_view(['GET'])
def menu_items(request):
    items = MenuItem.objects.select_related('category').all()
    serialized = MenuItemSerializer(items, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def single_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    serialized = MenuItemSerializer(item)
    return Response(serialized.data)
