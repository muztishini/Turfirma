from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Customers, Tours, Transport, Excursions, Hotels, Bookings, Payments, Reviews


# класс кастомизации админки клиентов
@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customers._meta.fields]
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ['phone', 'last_name']
    list_per_page = 10


# класс кастомизации админки экскурсий
@admin.register(Excursions)
class ExcursionsAdmin(admin.ModelAdmin):
    list_display = ('excursion_name', 'get_description', 'excursion_date', 'price', 'photo_excur', 'get_image')
    fields = ('excursion_name', 'description', 'excursion_date', 'price', 'photo_excur', 'get_image')
    readonly_fields = ('get_image',)
    list_per_page = 10

    @admin.display(description="Изображение")
    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.photo_excur.url}' width=50>")

    @admin.display(description="Описание")
    def get_description(self, obj):
        return obj.description[:50]


# класс кастомизации админки отелей
@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'address', 'rating', 'contact_number', 'photo_hotel', 'get_image']
    list_per_page = 10

    @admin.display(description="Изображение")
    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.photo_hotel.url}' width=50>")


# класс кастомизации админки транспорта
@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Transport._meta.fields]
    list_per_page = 10


# класс кастомизации админки бронирования
@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_link', 'tour_link', 'booking_date', 'status']
    list_editable = ('status',)
    list_per_page = 10

    @admin.display(description='Клиент')
    def customer_link(self, obj):
        link = f"<a href='/admin/turfirmaapp/customers/{obj.customer.id}/change/'>{obj.customer.last_name} {obj.customer.first_name}</a>"
        return format_html(link)

    customer_link.admin_order_field = 'customer__last_name'

    @admin.display(description='Тур')
    def tour_link(self, obj):
        link = f"<a href='/admin/turfirmaapp/tours/{obj.tour.id}/change/'>{obj.tour.tour_name}</a>"
        return format_html(link)

    tour_link.admin_order_field = 'tour__tour_name'


# класс кастомизации админки платежей
@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'booking_link', 'payment_date', 'amount', 'payment_method']
    list_display_links = ['id']
    list_per_page = 10

    @admin.display(description='Id бронирования')
    def booking_link(self, obj):
        link = f"<a href='/admin/turfirmaapp/bookings/{obj.booking.id}/change/'>{obj.booking.id}</a>"
        return format_html(link)


# класс кастомизации админки туров
@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ['tour_name', 'get_description', 'start_date', 'end_date', 'price', 'photo_tour', 'get_image',
                    'excursions_list', 'transport_links', 'hotel_links']
    fields = (
        'tour_name', 'description', 'start_date', 'end_date', 'price', 'photo_tour', 'excursions', 'transport', 'hotel')
    readonly_fields = ('get_image',)
    list_per_page = 10

    @admin.display(description="Описание")
    def get_description(self, obj):
        return obj.description[:50]

    @admin.display(description="Изображение")
    def get_image(self, obj):
        if obj.photo_tour:
            return mark_safe(f"<img src='{obj.photo_tour.url}' width=50>")
        return "Нет изображения"

    @admin.display(description='Экскурсии')
    def excursions_list(self, obj):
        excur_links = []
        for excur in obj.excursions.all():
            link = f"<a href='/admin/turfirmaapp/excursions/{excur.id}/change/'>{excur.excursion_name}</a>"
            excur_links.append(link)
        return format_html(", ".join(excur_links)) if excur_links else "Нет экскурсий"

    @admin.display(description='ID транспорта')
    def transport_links(self, obj):
        link = f"<a href='/admin/turfirmaapp/transport/{obj.transport.id}/change/'>{obj.transport.id}</a>"
        return format_html(link)

    @admin.display(description='Отель')
    def hotel_links(self, obj):
        link = f"<a href='/admin/turfirmaapp/hotels/{obj.hotel.id}/change/'>{obj.hotel.hotel_name}</a>"
        return format_html(link)


# класс кастомизации админки отзывов
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_reviews', 'date_review']
    list_per_page = 10

    @admin.display(description="Отзыв")
    def get_reviews(self, obj):
        return obj.review[:50]


admin.site.site_title = 'Админ-панель сайта турфирмы'
admin.site.site_header = 'Админ-панель сайта турфирмы'
admin.site.site_url = 'http://127.0.0.1:8000/'
