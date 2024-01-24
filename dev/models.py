from django.db import models
from django_country_kit.fields import CountryField

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()

    def __str__(self):
        return self.name