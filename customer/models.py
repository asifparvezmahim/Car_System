from django.db import models
from django.contrib.auth.models import User
from cars.models import Car


# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField()

    def __str__(self):
        return self.Name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car = models.ManyToManyField(Car)

    def __str__(self):
        return self.user.username
