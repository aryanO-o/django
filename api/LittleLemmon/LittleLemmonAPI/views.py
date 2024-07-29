from django.shortcuts import render
from rest_framework import generics
from .models import MenuItems
from .serializers import MenuItemsSerializer

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer
