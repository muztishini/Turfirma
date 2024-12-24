from django.urls import path
from .views import index, about, tours


urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('tours', tours, name='tours'),
]
