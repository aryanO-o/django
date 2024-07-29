from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class Home(View):
    def get(self, request):
        return HttpResponse("new home page")
    
    def post(self, request):
        return HttpResponse("new home page")