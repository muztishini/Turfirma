from django.urls import path
from .views import (home, about, contact, reviews, tours, show_tour, booking, excursions, show_excursion, hotels, show_hotel,
                    register_customers, login, logout_user)


# список путей приложения
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('reviews', reviews, name='reviews'),
    path('tours', tours, name='tours'),
    path('tours/<int:tour_id>/', show_tour, name='tour'),
    path('booking', booking, name='booking'),
    path('excursions', excursions, name='excursions'),
    path('excursions/<int:excursion_id>/', show_excursion, name='excursion'),
    path('hotels', hotels, name='hotels'),
    path('hotels/<int:hotel_id>/', show_hotel, name='hotel'),
    path('register', register_customers, name='register'),
    path('login', login, name='login'),
    path('logout', logout_user, name='logout'),
]
