from django.shortcuts import redirect, render
from .forms import CustomersForm, LoginForm
from .models import Hotels, Tours, Excursions, Transport, Customers
from datetime import date


def set_session_data(request, customer):
    request.session['customer'] = customer
    return render(request, 'base.html')


def index(request):
    my_data = request.session.get('customer', None)
    return render(request, 'index.html', {'customer': my_data})


def about(request):
    my_data = request.session.get('customer', None)
    return render(request, 'about.html', {'customer': my_data})


def contact(request):
    my_data = request.session.get('customer', None)
    return render(request, 'contact.html', {'customer': my_data})


def tours(request):
    data = Tours.objects.all()
    my_data = request.session.get('customer', None)
    return render(request, "tours.html", {"data": data, 'customer': my_data})


def show_tour(request, tour_id):
    try:
        my_data = request.session.get('customer', None)
        data_tour = Tours.objects.get(id=tour_id)
        data_excursion = Tours.objects.get(id=tour_id).excursions.all()
        data_transport = Transport.objects.get(id=data_tour.transport_id)
        data_hotel = Hotels.objects.get(id=data_tour.hotel_id)
        return render(request, "show_tour.html",
                      {"data_tour": data_tour, "data_excursion": data_excursion, "data_transport": data_transport,
                       "data_hotel": data_hotel, 'customer': my_data})
    except Exception as e:
        print(e)
        return render(request, '404.html')


def booking(request):
    my_data = request.session.get('customer', None)
    return render(request, 'booking.html', {'customer': my_data})


def excursions(request):
    data = Excursions.objects.all()
    my_data = request.session.get('customer', None)
    return render(request, "excursions.html", {"data": data, 'customer': my_data})


def show_excursion(request, excursion_id):
    try:
        my_data = request.session.get('customer', None)
        data = Excursions.objects.get(id=excursion_id)
        return render(request, "show_excursion.html", {"data": data, 'customer': my_data})
    except:
        return render(request, '404.html')


def hotels(request):
    my_data = request.session.get('customer', None)
    data = Hotels.objects.all()
    return render(request, "hotels.html", {"data": data, 'customer': my_data})


def show_hotel(request, hotel_id):
    try:
        my_data = request.session.get('customer', None)
        data = Hotels.objects.get(id=hotel_id)
        return render(request, "show_hotel.html", {"data": data, 'customer': my_data})
    except Exception as e:
        print(e)
        return render(request, '404.html')


def register_customers(request):
    my_data = request.session.get('customer', None)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        registration_date = date.today()
        customer = Customers.objects.create(
           first_name = first_name,
            last_name = last_name,
           email = email,
           phone = phone,
           registration_date = registration_date 
        )
        data = "Вы успешно зарегистрировались!"
        return render(request, "register.html", {"data": data, 'customer': my_data})
    else:
        outperform = CustomersForm()
        return render(request, "register.html", {"form": outperform})


def login(request):
    my_data = request.session.get('customer', None)
    outperform = LoginForm()
    if request.method == "POST":
        phone = request.POST.get("phone")
        try:
            customer = Customers.objects.get(phone=phone)
            set_session_data(request, customer=customer.first_name)
            return render(request, 'booking.html', {"customer": customer.first_name})
        except:
            message = "Нет такого клиента"
            return render(request, 'login.html', {"form": outperform, "message": message})
    else:        
        return render(request, 'login.html', {"form": outperform, "customer": my_data})


def logout_user(request):
    set_session_data(request, customer=None)
    return redirect('home')
