# Generated by Django 4.2.7 on 2023-12-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='cars/media/uploads/'),
        ),
    ]
