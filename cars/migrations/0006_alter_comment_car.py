# Generated by Django 4.2.7 on 2023-12-22 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_comment_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cars.car'),
        ),
    ]
