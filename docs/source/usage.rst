Usage
=====

Django Country Kit provides the following features for usage:

Country Model Field
-------------------

In your models, use the ``CountryField`` to store country codes:

.. code-block:: python

    from django.db import models
    from django_country_kit.fields import CountryField
    
    class YourModel(models.Model):
        country = CountryField()

For multiple selections:

.. code-block:: python

    from django.db import models
    from django_country_kit.fields import CountryField
    
    class YourModel(models.Model):
        countries = CountryField(multiple=True)

Country Widget
---------------

In your forms, use the ``CountryWidget`` to render a dropdown list of countries:

.. code-block:: python

    from django import forms
    from django_country_kit.widgets import CountryWidget
    
    class YourForm(forms.Form):
        country = forms.CharField(widget=CountryWidget())

For multiple selections:

.. code-block:: python

    from django import forms
    from django_country_kit.widgets import MultipleCountryWidget
    
    class YourForm(forms.Form):
        countries = forms.CharField(widget=MultipleCountryWidget())

Country Class
--------------

The ``Country`` class represents a country and provides properties for accessing its name, alpha3, and code. This class is part of the Django Country Kit and offers convenient functionality for handling country-related data.


You can create an instance of the ``Country`` class to retrieve information about a specific country. Here's how you can use it:

.. code-block:: python

    from django_country_kit.base import Country

    # Create a Country instance with a specific country code
    country = Country(code='US')

    # Retrieve the name of the country
    country_name = country.name  # Returns 'United States'

    # Retrieve the alpha3 code of the country
    country_alpha3 = country.alpha3  # Returns 'USA'

Or you can create by country name:

.. code-block:: python

    from django_country_kit.base import Country

    # Create a Country instance with a country name
    country = Country(name='United States')

    # Retrieve the code of the country
    country_name = country.code  # Returns 'United States'

    # Retrieve the alpha3 code of the country
    country_alpha3 = country.alpha3  # Returns 'USA'
