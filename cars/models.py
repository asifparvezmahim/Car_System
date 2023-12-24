from django.db import models
from brands.models import Brand


# Create your models here.
class Car(models.Model):
    Car_Name = models.CharField(max_length=20)
    Price = models.CharField(max_length=35)
    Quantity = models.IntegerField()
    Description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="cars/media/uploads/", blank=True, null=True)

    def __str__(self):
        return self.Car_Name


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"
