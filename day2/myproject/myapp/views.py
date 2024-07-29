from django.shortcuts import render

from django.http import HttpResponse

from datetime import datetime
# Create your views here.

def home(request):
    response = HttpResponse("this works")
    response.headers['age'] = 120
    msg = f"<br>response: {response} and <br>response.header: {response.headers}"
    return HttpResponse(msg, content_type='text/html', charset='utf-8')



def say_hello(request):
    return HttpResponse('hello')

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(f'The current year is {date_joined}')

def menu(request):
    text = """<h1 style='color:blue;'>Welcome to my app</h1>"""
    return HttpResponse(text)

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a staple food of traditional Italian cuisine, with the first reference dating to 1154 in Sicily.',
        'falafel': 'Falafel is a traditional Middle Eastern food, commonly served in a pita, which acts as a pocket, or wrapped in a flatbread known as taboon.',
        'cheesecake': 'Cheesecake is a sweet dessert consisting of one or more layers. The main, and thickest layer, consists of a mixture of soft, fresh cheese, eggs, and sugar.',
    }
    description = items.get(dish, 'The dish is not available')
    return HttpResponse(f'<h2>{dish}</h2><p>{description}</p>')