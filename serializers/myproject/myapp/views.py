from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MenuItem
from rest_framework.decorators import api_view
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view()
def menu_list(request):
    menu_items = MenuItem.objects.all()
    serialised_items = MenuItemSerializer(menu_items, many=True)
    return Response(serialised_items.data)

@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)