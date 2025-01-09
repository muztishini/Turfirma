from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Customers, Tours, Transport, Excursions, Hotels, Bookings, Payments


list_models = [Customers, Bookings, Payments]
admin.site.register(list_models)


@admin.register(Excursions)
class ExcursionsAdmin(admin.ModelAdmin):
    list_display = ('excursion_name', 'description', 'excursion_date',  'price', 'photo_excur', 'get_image')
    fields = ('excursion_name', 'description', 'excursion_date', 'price', 'photo_excur', 'get_image')
    readonly_fields = ('get_image',)

    @admin.display(description="Изображение")
    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.photo_excur.url}' width=50>")


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    ...


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Transport._meta.fields]


@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ['tour_name', 'description', 'start_date', 'end_date', 'price', 'photo_tour', 'get_image', 'excursions_list', 'transport', 'hotel']
    fields = ('tour_name', 'description', 'start_date', 'end_date', 'price', 'photo_tour', 'get_image', 'excursions_list', 'transport', 'hotel')
    readonly_fields = ('get_image',)

    @admin.display(description="Изображение")
    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.photo_tour.url}' width=50>")
    
    @admin.display(description='Экскурсии')
    def excursions_list(self, obj):
        return ", ".join([excursion.excursion_name for excursion in obj.excursions.all()])


admin.site.site_title = 'Админ-панель сайта турфирмы'
admin.site.site_header = 'Админ-панель сайта турфирмы'
admin.site.site_url = 'http://127.0.0.1:8000/'
