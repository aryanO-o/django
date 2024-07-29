from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.say_hello, name='hello'),
    path('display_date/', views.display_date, name='date'),
    path('menu/', views.menu, name='menu'),
    path('dishes/<str:dish>', views.menuitems)
]