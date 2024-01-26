"""
Module defining a Country class and a CountryField model field with internationalization support.

This module defines the 'Country' class, which is a simple class representing a country with properties
to access its name and alpha3 code. It also defines the 'CountryField' model field, a subclass of
Django's CharField, designed for storing country codes with internationalization support.

Usage:
- Include this module in your Django app.
- Use the 'Country' class to represent countries and the 'CountryField' in your models.

Example:
    # In your Django app's models.py file:
    from django.db import models
    from .countries import CountryField

    class ExampleModel(models.Model):
        name = models.CharField(max_length=255)
        country = CountryField()

Attributes:
    - Country (class): A class representing a country with properties for accessing its name and alpha3 code.
    - CountryField (class): A model field for storing country codes with internationalization support.
        It inherits from Django's CharField and uses choices from the 'COUNTRIES' data.

Note:
    The 'Country' class uses the 'COUNTRIES' data for country information.
    Make sure to include this module in your project and set up internationalization in your Django app.

For more information, see Django documentation on models and model fields:
https://docs.djangoproject.com/en/5.0/topics/db/models/
https://docs.djangoproject.com/en/5.0/ref/models/fields/
"""

from django import forms
from django.db.models.fields import CharField

from .base import Country
from .widgets import CountryWidget


class CountryField(CharField):
    """
    A model field for storing country codes with internationalization support.

    Attributes:
        - max_length (int): The maximum length of the country code (2 characters).
        - choices (generator): The choices for the country field, generated from the 'COUNTRIES' data.
    """

    def __init__(self, *args, **kwargs):
        self.countries = Country().countries_data
        kwargs['max_length'] = max(len(code) for code in self.countries)
        kwargs['choices'] = ((code, data['name']) for code, data in self.countries.items())
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'choices': kwargs.pop('choices', self.choices),
            'widget': CountryWidget,
            'choices_form_class': forms.TypedChoiceField,
            "form_class": forms.ChoiceField,
        }
        defaults.update(kwargs)

        return super().formfield(**defaults)
