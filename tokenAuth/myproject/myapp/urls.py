from django.urls import path

from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', views.menu_items),
    path('menu/<int:pk>/', views.single_item),
    path('secret', views.secret),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('manager-view/', views.manager_view),
    path('throttle-check', views.throttle_check),
]