from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menu_items),
    path('menu/<int:pk>/', views.single_item),
]