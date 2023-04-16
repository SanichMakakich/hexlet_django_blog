# *hexlet_django_blog/views.py*
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def about(request):
    return render(request, 'about.html')
