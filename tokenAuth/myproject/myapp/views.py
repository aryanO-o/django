from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, throttle_classes
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from .throttles import TenCallsPerMinute


from .models import MenuItem
from .serializers import MenuItemSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Create your views here.

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')

        #ordering
        ordering = request.query_params.get('ordering')

        #pagination
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)

        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price) #lte = less than or equal to
        
        if search:
            items = items.filter(title__istartswith=search)
        
        if ordering:
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields)

        #paginate
        paginator = Paginator(items, per_page = perpage)
        try:
            items = paginator.page(number = page)
        except EmptyPage:
            items = []

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

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message': 'This is a secret message!'})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Managers').exists():
        return Response({'message': 'Welcome, Manager!'})
    else:
        return Response({'message': 'You are not a manager!'}, status=403)


@api_view(['GET', 'POST'])
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message': 'success'})


@api_view(['GET', 'POST'])
@throttle_classes([TenCallsPerMinute])
def user_throttle_check(request):
    return Response({'message': 'success auth user'})
#naman : "1c86d337eb22e6f08a921aabbd6042ea39da710e"
#naman2 : "ac8199a4e7023a7202e7680c7f4512f3159e829f"