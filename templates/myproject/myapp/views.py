from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu

# Create your views here.

def hello(request):
    return HttpResponse('Hello, World!')

def about(request):
    about_content = {
        'about': 'This is a simple Django web application. It is a part of the Django tutorial series.'
    }
    return render(request, 'about.html', about_content)

# def menu(request):
#     menuitem = {
#         'mains':[
#             {'name': 'Samosa', 'price': 10},
#             {'name': 'Burger', 'price': 25},
#             {'name': 'Pizza', 'price': 95},
#             {'name': 'Pasta', 'price': 75},
#             {'name': 'Dosa', 'price': 40},
#             {'name': 'Idli', 'price': 30},
            
#         ]
#     }
#     return render(request, 'menu.html', menuitem)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_cards.html', newmenu_dict)