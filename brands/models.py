from django.db import models


# Create your models here.
class Brand(models.Model):
    Name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self):
        return self.Name
