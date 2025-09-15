from django.shortcuts import redirect, render, get_object_or_404
from .forms import CustomersForm, LoginForm, ReviewForm, ApplicationForm
from .models import Hotels, Tours, Excursions, Transport, Customers, Bookings, Reviews, Application
from datetime import date


# функция обработки сессии
def set_session_data(request, customer_name, customer_id):
    request.session['customer'] = customer_name
    request.session['customer_id'] = customer_id
    return render(request, 'base.html')


# функция представления домашней страницы
def home(request):
    my_data = request.session.get('customer', None)
    return render(request, 'home.html', {'customer': my_data})


# функция представления страницы "о нас"
def about(request):
    my_data = request.session.get('customer', None)
    return render(request, 'about.html', {'customer': my_data})


# функция представления страницы контактов
def contact(request):
    my_data = request.session.get('customer', None)
    return render(request, 'contact.html', {'customer': my_data})


# функция представления страницы отзывов
def reviews(request):
    my_data = request.session.get('customer', None)
    outperform = ReviewForm(request.POST, request.FILES)
    data = Reviews.objects.all().order_by('-id')
    if request.method == "POST":
        if outperform.is_valid():
            outperform.save()
            return render(request, 'reviews.html', {'form': outperform, "data": data, 'customer': my_data})
        data = Reviews.objects.all().order_by('-id')
        return render(request, 'reviews.html', {"form": outperform, "data": data, 'customer': my_data})
    else:
        return render(request, 'reviews.html', {"form": outperform, "data": data, "customer": my_data})


# функция представления страницы туров
def tours(request):
    data = Tours.objects.all()
    my_data = request.session.get('customer', None)
    return render(request, "tours.html", {"data": data, 'customer': my_data})


# функция представления страницы выбранного тура
def show_tour(request, tour_id):
    try:
        my_data = request.session.get('customer', None)
        data_tour = Tours.objects.get(id=tour_id)
        data_excursion = Tours.objects.get(id=tour_id).excursions.all()
        data_transport = Transport.objects.get(id=data_tour.transport_id)
        data_hotel = Hotels.objects.get(id=data_tour.hotel_id)
        request.session['tour_id'] = tour_id
        quantity = Tours.objects.get(id=tour_id).number_of_views
        Tours.objects.filter(id=tour_id).update(number_of_views=quantity + 1)
        return render(request, "show_tour.html",
                      {"data_tour": data_tour, "data_excursion": data_excursion, "data_transport": data_transport,
                       "data_hotel": data_hotel, 'customer': my_data})
    except Exception as e:
        print(e)
        return render(request, '404.html')


# функция представления страницы бронирования
def booking(request):
    my_data = request.session.get('customer', None)
    cust_id = request.session.get('customer_id')
    tour_id = request.session.get('tour_id')
    tour_name = Tours.objects.get(id=tour_id).tour_name
    booking_in_base = Bookings.objects.filter(customer=cust_id, tour=tour_id)
    if not booking_in_base:
        if cust_id is not None:
            Bookings.objects.create(
                customer_id=cust_id,
                tour_id=tour_id,
                booking_date=date.today(),
                status="забронировано"
            )
            return render(request, 'booking.html', {'customer': my_data, 'tour_name': tour_name})
        else:
            form = ApplicationForm()
            if request.method == "POST":
                name = request.POST.get("name")
                phone = request.POST.get("phone")
                print(tour_id, tour_name)
                tour_obj = get_object_or_404(Tours, id=tour_id)
                Application.objects.create(
                    name=name,
                    phone=phone,
                    tour=tour_obj,
                    application_date=date.today()
                )
                return render(request, 'application.html', {'customer': my_data})
    else:
        return render(request, 'booking.html', {'customer': my_data, 'tour_name': tour_name, 'flag': 1, "form": form})
    return render(request, 'booking.html', {'customer': my_data, "form": form})


# функция представления страницы экскурсий
def excursions(request):
    data = Excursions.objects.all()
    my_data = request.session.get('customer', None)
    return render(request, "excursions.html", {"data": data, 'customer': my_data})


# функция представления страницы выбранной экскурсии
def show_excursion(request, excursion_id):
    try:
        my_data = request.session.get('customer', None)
        data = Excursions.objects.get(id=excursion_id)
        data_tours = data.tours_set.all()
        return render(request, "show_excursion.html", {"data": data, "data_tours": data_tours, 'customer': my_data})
    except Exception as e:
        print(e)
        return render(request, '404.html')


# функция представления страницы отелей
def hotels(request):
    my_data = request.session.get('customer', None)
    data = Hotels.objects.all()
    return render(request, "hotels.html", {"data": data, 'customer': my_data})


# функция представления страницы выбранного отеля
def show_hotel(request, hotel_id):
    try:
        my_data = request.session.get('customer', None)
        data = Hotels.objects.get(id=hotel_id)
        return render(request, "show_hotel.html", {"data": data, 'customer': my_data})
    except Exception as e:
        print(e)
        return render(request, '404.html')


# функция представления страницы регистрации клиента
def register_customers(request):
    outperform = CustomersForm()
    my_data = request.session.get('customer', None)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        registration_date = date.today()
        try:
            customer = Customers.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                registration_date=registration_date
            )
            set_session_data(
                request, customer_name=customer.first_name, customer_id=customer.id)
            return render(request, "register.html", {'customer': customer.first_name})
        except Exception as e:
            print(e)
            error = "Пользователь с таким email или номером телефона уже зарегистрирован!"
            return render(request, "register.html", {"form": outperform, 'error': error})
    else:
        return render(request, "register.html", {"form": outperform, "customer": my_data})


# функция представления страницы логина клиента
def login(request):
    my_data = request.session.get('customer', None)
    outperform = LoginForm()
    if request.method == "POST":
        phone = request.POST.get("phone")
        try:
            customer = Customers.objects.get(phone=phone)
            set_session_data(
                request, customer_name=customer.first_name, customer_id=customer.id)
            return render(request, 'login.html', {"customer": customer.first_name})
        except Exception as e:
            print(e)
            message = "Извините, пользователь с данным номером телефона не найден."
            return render(request, 'login.html', {"form": outperform, "message": message})
    else:
        return render(request, 'login.html', {"form": outperform, "customer": my_data})


# функция представления страницы выхода клиента
def logout_user(request):
    set_session_data(request, customer_name=None, customer_id=None)
    return redirect('home')
