from django.contrib import admin
from .models import *


admin.site.register(Customers)
admin.site.register(Tours)
admin.site.register(Transport)
admin.site.register(Excursions)
admin.site.register(Hotels)
admin.site.register(HotelExcursion)
admin.site.register(Bookings)
admin.site.register(Payments)

admin.site.site_title = 'Админ-панель сайта турфирмы'
admin.site.site_header = 'Админ-панель сайта турфирмы'
admin.site.site_url = 'http://127.0.0.1:8000/turfirma/'
