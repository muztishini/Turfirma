from django.urls import path
from .views import index, about, tours, show_tour, booking, excursions, show_excursion, hotels, show_hotel


urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('tours', tours, name='tours'),
    path('tours/<int:tour_id>/', show_tour, name='tour'),
    path('booking', booking, name='booking'),
    path('excursions', excursions, name='excursions'),
    path('excursions/<int:excursion_id>/', show_excursion, name='excursion'),
    path('hotels', hotels, name='hotels'),
    path('hotels/<int:hotel_id>/', show_hotel, name='hotel'),
]
