# Generated by Django 4.2.7 on 2023-12-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
