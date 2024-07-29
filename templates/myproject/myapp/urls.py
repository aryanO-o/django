from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('hello/', views.hello, name='hello'),
    # path('menu/', views.menu, name='menu'),
    path('menu_card/', views.menu_by_id, name='menu_by_id'),
]