from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Customers, Tours, Transport, Excursions, Hotels, HotelExcursion, Bookings, Payments


list_models = [Customers, Transport, HotelExcursion, Bookings, Payments]
admin.site.register(list_models)


@admin.register(Excursions)
class ExcursonsAdmin(admin.ModelAdmin):
    ...


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    ...


@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('tour_name', 'description', 'start_date', 'end_date', 'price', 'photo_tour', 'get_image')
    fields = ('tour_name', 'description', 'start_date', 'end_date', 'price', 'photo_tour', 'get_image')
    readonly_fields = ('get_image',)

    @admin.display(description="Изображение")
    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.photo_tour.url}' width=50>")


admin.site.site_title = 'Админ-панель сайта турфирмы'
admin.site.site_header = 'Админ-панель сайта турфирмы'
admin.site.site_url = 'http://127.0.0.1:8000/'
