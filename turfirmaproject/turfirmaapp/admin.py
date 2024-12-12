from django.contrib import admin
from .models import *


admin.site.register(Customers)
admin.site.register(Tours)
admin.site.register(Transport)
admin.site.register(Excursions)
admin.site.register(Hotels)
# admin.site.register(HotelExcursion)
admin.site.register(Bookings)
admin.site.register(Payments)
