# Generated by Django 4.0.5 on 2022-07-25 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoViajesApp', '0004_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acerca_de',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]
