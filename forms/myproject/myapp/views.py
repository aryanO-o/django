from django.shortcuts import render
from django.http import HttpResponse

from myapp.forms import LogForm

# Create your views here.

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data saved')
    context = {'form': form}
    return render(request, 'home.html', context)
