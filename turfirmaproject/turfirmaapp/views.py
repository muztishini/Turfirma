from django.shortcuts import render
from .models import Tours


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def tours(request):
    data = Tours.objects.all()
    return render(request, "tours.html", {"data" : data})
