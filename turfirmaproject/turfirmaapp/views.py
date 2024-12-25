from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Tours


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def tours(request):
    data = Tours.objects.all()
    return render(request, "tours.html", {"data" : data})


def show_tour(request, tour_id):
    data = get_object_or_404(Tours, id=tour_id)
    return render(request, "show_tour.html", {"data" : data})
  

def booking(request):
    return render(request, 'booking.html')
