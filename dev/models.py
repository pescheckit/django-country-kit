"""
Django Model for ExampleModel.

This model represents an example entity in the database, with fields such as 'name'
and 'country'. It utilizes the Django Country Kit's 'CountryField' for handling country
information.

Usage:
- Include this model in your Django app's models.py file.
- Make migrations and apply them to create the corresponding database table.

Example:
    # In your Django app's models.py file:
    from django.db import models
    from django_country_kit.fields import CountryField

    class ExampleModel(models.Model):
        name = models.CharField(max_length=255)
        country = CountryField()

        def __str__(self):
            return self.name

Attributes:
    - name (CharField): A character field for storing the name of the entity.
    - country (CountryField): A custom field from Django Country Kit for handling country information.

Methods:
    - __str__(): A method returning a string representation of the entity.

Note:
    Make sure to install the 'django-country-kit' package and include it in your project's
    dependencies before using the 'CountryField'. You can install it using:
    pip install django-country-kit

For more information, see Django documentation on models:
https://docs.djangoproject.com/en/5.0/topics/db/models/
"""
from django.db import models

from django_country_kit.fields import CountryField


# Create your models here.
class ExampleModel(models.Model):
    """
    Django Model for ExampleModel.

    Attributes:
        - name (CharField): A character field for storing the name of the entity.
        - country (CountryField): A custom field from Django Country Kit for handling country information.
    """
    name = models.CharField(max_length=255)
    country = CountryField()

    def __str__(self):
        """
        Return a string representation of the entity.
        """
        return str(self.name)
