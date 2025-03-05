# Generated by Django 5.1.6 on 2025-03-05 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfirmaapp', '0004_tours_excursions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='Anonymous', max_length=50, verbose_name='Пользователь')),
                ('review', models.CharField(max_length=255, verbose_name='Отзыв')),
                ('data', models.DateField(verbose_name='Дата отзыва')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
        migrations.AlterField(
            model_name='bookings',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfirmaapp.customers', verbose_name='Имя клиента'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='status',
            field=models.CharField(choices=[('забронировано', 'Забронировано'), ('оплачено', 'Оплачено'), ('подтверждено', 'Подтверждено'), ('посетил', 'Посетил'), ('отклонено', 'Отклонено')], max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfirmaapp.tours', verbose_name='Название тура'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('карта', 'Карта'), ('наличные', 'Наличные'), ('перевод', 'Перевод'), ('qr-код', 'QR-код')], max_length=50, null=True, verbose_name='Метод оплаты'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='excursions',
            field=models.ManyToManyField(blank=True, to='turfirmaapp.excursions', verbose_name='Название экскурсии'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfirmaapp.hotels', verbose_name='название отеля'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='transport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfirmaapp.transport', verbose_name='ID транспорта'),
        ),
    ]
