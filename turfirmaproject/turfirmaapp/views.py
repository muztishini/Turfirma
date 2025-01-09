from django.shortcuts import render
from .models import Tours, Excursions


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def tours(request):
    data = Tours.objects.all()
    return render(request, "tours.html", {"data": data})


def show_tour(request, tour_id):
    try:
        data_tour = Tours.objects.get(id=tour_id)
        data_excursion = Tours.objects.get(id=tour_id).excursions.all()
        print(data_tour, data_excursion)
        return render(request, "show_tour.html", {"data_tour": data_tour, "data_excursion": data_excursion})
    except:
        return render(request, '404.html')


def booking(request):
    return render(request, 'booking.html')


def excursions(request):
    data = Excursions.objects.all()
    return render(request, "excursions.html", {"data": data})


def show_excursion(request, excursion_id):
    try:
        data = Excursions.objects.get(id=excursion_id)
        return render(request, "show_excursion.html", {"data": data})
    except:
        return render(request, '404.html')
