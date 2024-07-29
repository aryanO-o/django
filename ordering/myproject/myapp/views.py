from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price) #lte = less than or equal to
        
        if search:
            items = items.filter(title__istartswith=search)
        
        if ordering:
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields)

        serialized = MenuItemSerializer(items, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = MenuItemSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        return Response(serialized.errors, status=400)


@api_view(['GET', 'POST'])
def single_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    serialized = MenuItemSerializer(item)
    return Response(serialized.data)