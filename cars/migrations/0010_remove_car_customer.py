# Generated by Django 4.2.7 on 2023-12-23 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='customer',
        ),
    ]
