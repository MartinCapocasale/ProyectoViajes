# Generated by Django 4.0.5 on 2022-06-27 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoViajesApp', '0002_excursion_imagen_hotel_imagen_vuelo_imagen_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excursion',
            options={'verbose_name_plural': 'Excursiones'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name_plural': 'Hoteles'},
        ),
    ]
