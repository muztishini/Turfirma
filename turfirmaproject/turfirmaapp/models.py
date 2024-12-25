from django.db import models
from django.urls import reverse


class Customers(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон")
    registration_date = models.DateField(verbose_name="Дата регистрации")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = "Клиенты"


class Tours(models.Model):
    tour_name = models.CharField(max_length=100, verbose_name="Название тура")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    photo_tour = models.ImageField(upload_to="photo_tour/", verbose_name="Фотография", null=True)
    
    def get_absolute_url(self):
        return reverse('tour', kwargs={'tour_id': self.pk})

    def __str__(self):
        return self.tour_name

    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = "Туры"


class Excursions(models.Model):
    excursion_name = models.CharField(max_length=100, verbose_name="Название экскурсии")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    excursion_date = models.DateField(verbose_name="Дата экскурсии")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    photo_excur = models.ImageField(upload_to="photo_excur/", verbose_name="Фотография", null=True)

    def __str__(self):
        return self.excursion_name

    class Meta:
        verbose_name = 'экскурсию'
        verbose_name_plural = "Экскурсии"


class Hotels(models.Model):
    hotel_name = models.CharField(max_length=100, verbose_name="Название отеля")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес")
    rating = models.IntegerField(null=True, blank=True, verbose_name="Рейтинг")
    contact_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Контактный телефон")
    photo_hotel = models.ImageField(upload_to="photo_hotel/", verbose_name="Фотография", null=True)

    def __str__(self):
        return self.hotel_name

    class Meta:
        verbose_name = 'отель'
        verbose_name_plural = "Отели"


class Transport(models.Model):
    transport_type = models.CharField(max_length=50, verbose_name="Тип транспорта")
    company_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Название компании")
    flight_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="Номер рейса")
    departure_time = models.DateTimeField(null=True, blank=True, verbose_name="Время отправления")
    arrival_time = models.DateTimeField(null=True, blank=True, verbose_name="Время прибытия")

    def __str__(self):
        return self.transport_type

    class Meta:
        verbose_name = 'транспорт'
        verbose_name_plural = "Транспорт"


class Bookings(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="Id клиента")
    tour_id = models.ForeignKey(Tours, on_delete=models.CASCADE, verbose_name="Id тура")
    booking_date = models.DateField(verbose_name="Дата бронирования")
    status = models.CharField(max_length=20, verbose_name="Статус")

    class Meta:
        verbose_name = 'бронирование'
        verbose_name_plural = "Бронирования"


class Payments(models.Model):
    booking_id = models.ForeignKey(Bookings, on_delete=models.CASCADE, verbose_name="Id бронирования")
    payment_date = models.DateField(verbose_name="Дата оплаты")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    payment_method = models.CharField(max_length=50, null=True, blank=True, verbose_name="Метод оплаты")

    class Meta:
        verbose_name = 'оплату'
        verbose_name_plural = "Оплаты"


class HotelExcursion(models.Model):
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    excursion_id = models.ForeignKey(Excursions, on_delete=models.CASCADE)
