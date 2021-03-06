# Generated by Django 4.0.5 on 2022-06-26 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=150)),
                ('duracion', models.DateTimeField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=150)),
                ('desde', models.DateTimeField()),
                ('hasta', models.DateTimeField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vuelo', models.IntegerField()),
                ('origen', models.CharField(max_length=30)),
                ('destino', models.CharField(max_length=30)),
                ('ida', models.DateTimeField()),
                ('vuelta', models.DateTimeField()),
                ('precio', models.FloatField()),
            ],
        ),
    ]
