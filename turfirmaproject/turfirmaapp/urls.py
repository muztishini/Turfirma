from django.urls import path
from .views import index, about, tours, show_tour, booking


urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('tours', tours, name='tours'),
    path('tours/<int:tour_id>/', show_tour, name='tour'),
    path('booking', booking, name='booking'),
]
