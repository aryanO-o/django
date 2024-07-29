from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.form_view, name='form_view'),
]