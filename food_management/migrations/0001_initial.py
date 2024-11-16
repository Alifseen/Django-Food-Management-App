# Generated by Django 5.1.3 on 2024-11-15 15:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=1000, unique=True)),
                ('ingredients', models.CharField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dish_category', models.CharField(choices=[('starter', 'Starter'), ('salads', 'Salads'), ('entree', 'Entree'), ('dessert', 'Dessert')], max_length=200)),
                ('availability', models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Available')], default=1)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]