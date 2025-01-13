from django.shortcuts import render
from .models import Hotels, Tours, Excursions, Transport


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
        data_transport = Transport.objects.get(id=data_tour.transport_id)
        data_hotel = Hotels.objects.get(id=data_tour.hotel_id)
        return render(request, "show_tour.html", {"data_tour": data_tour, "data_excursion": data_excursion, "data_transport": data_transport, "data_hotel": data_hotel})
    except Exception as e:
        print(e)
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


def hotels(request):
    data = Hotels.objects.all()
    return render(request, "hotels.html", {"data": data})
 
    
def show_hotel(request, hotel_id):
    try:
        data = Hotels.objects.get(id=hotel_id)
        return render(request, "show_hotel.html", {"data": data})
    except:
        return render(request, '404.html')
    