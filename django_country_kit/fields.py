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

from django.db import models

from .data import COUNTRIES


class Country:
    """
    A class representing a country with properties for accessing its name and alpha3 code.

    Attributes:
        - _countries_data (dict): A dictionary containing information about various countries.
        - _code (str): The country code.
    """

    def __init__(self, code=None):
        self._countries_data = COUNTRIES
        self._code = code

    @property
    def countries_data(self):
        """Get the 'COUNTRIES' data."""
        return self._countries_data

    @property
    def name(self) -> str:
        """Get the name of the country."""
        return self._countries_data.get(self._code, {}).get('name', '')

    @property
    def alpha3(self) -> str:
        """Get the alpha3 code of the country."""
        return self._countries_data.get(self._code, {}).get('alpha3', '')


class CountryField(models.CharField):
    """
    A model field for storing country codes with internationalization support.

    Attributes:
        - max_length (int): The maximum length of the country code (2 characters).
        - choices (list): The choices for the country field, taken from the 'COUNTRIES' data.
    """

    def __init__(self, *args, **kwargs):
        # Set max_length to 2 for country codes
        kwargs['max_length'] = 2
        # Use choices from the COUNTRIES data
        kwargs['choices'] = [(code, data['name']) for code, data in Country().countries_data.items()]
        super().__init__(*args, **kwargs)
