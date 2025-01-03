from django.shortcuts import render
from .models import Tours, Excursions


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def tours(request):
    data = Tours.objects.all()
    return render(request, "tours.html", {"data" : data})


def show_tour(request, tour_id):
    try:
        data = Tours.objects.get(id=tour_id)
        return render(request, "show_tour.html", {"data" : data})
    except:
        return render(request, '404.html')


def booking(request):
    return render(request, 'booking.html')


def excursions(request):
    data = Excursions.objects.all()
    return render(request, "excursions.html", {"data" : data})


def show_excursion(request, excursion_id):
    try:
        data = Excursions.objects.get(id=excursion_id)
        return render(request, "show_excursion.html", {"data" : data})
    except:
        return render(request, '404.html')
