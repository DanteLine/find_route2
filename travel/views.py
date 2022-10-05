from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    name = 'Bob'

    return render(request, 'home.html', {'name': name})
def about(request):
    name = 'about my first project'

    return render(request, 'about.html', {'name': name})