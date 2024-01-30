# Django Country Kit

Django Country Kit is a Django app that provides country-related functionality, including a custom model field for storing country codes, a form widget for selecting countries, and associated tests.

## Features

- **Country Model Field:** Easily store and retrieve country codes in your Django models.
- **Country Widget:** A form widget for rendering a dropdown list of countries in your Django forms.

## Installation

1. Install Django Country Kit using pip:

    ```bash
    pip install django-country-kit
    ```

2. Add `'django_country_kit'` to your `INSTALLED_APPS` in your Django project's settings:

    ```python
    INSTALLED_APPS = [
        # ...
        'django_country_kit',
        # ...
    ]
    ```

3. Run collectstatic:

    ```bash
    python manage.py collectstatic
    ```


## Usage

### Country Model Field

In your models, use the `CountryField` to store country codes:

```python
from django.db import models
from django_country_kit.fields import CountryField

class YourModel(models.Model):
    country = CountryField()
```

For multiple selections:
```python
from django.db import models
from django_country_kit.fields import CountryField

class YourModel(models.Model):
    countries = CountryField(multiple=True)
```


### Country Widget

In your forms, use the `CountryWidget` to render a dropdown list of countries:

```python
from django import forms
from django_country_kit.widgets import CountryWidget

class YourForm(forms.Form):
    country = forms.CharField(widget=CountryWidget())
```

For multiple selections:
```python
from django import forms
from django_country_kit.widgets import MultipleCountryWidget

class YourForm(forms.Form):
    countries = forms.CharField(widget=MultipleCountryWidget())
```

## Country Class

The `Country` class represents a country and provides properties for accessing its name and alpha3 code. This class is part of the Django Country Kit and offers convenient functionality for handling country-related data.

### Usage

You can create an instance of the `Country` class to retrieve information about a specific country. Here's how you can use it:

```python
from django_country_kit.base import Country

# Create a Country instance with a specific country code
country = Country(code='US')

# Retrieve the name of the country
country_name = country.name  # Returns 'United States'

# Retrieve the alpha3 code of the country
country_alpha3 = country.alpha3  # Returns 'USA'
```

## Custom settings

Django Country Kit provides custom settings for further customization of country data:

- `OVERRIDE_COUNTRIES`: Allows users to override specific countries with custom data.
- `EXCLUDE_COUNTRIES`: Allows users to exclude specific countries from the available choices.
- `INCLUDE_COUNTRIES`: Allows users to include specific countries in the available choices.

You can customize these settings in your Django project's settings file to tailor the country data according to your needs.

We appreciate your feedback and contributions to improving Django Country Kit!


## Development

If you want to contribute to Django Country Kit, follow these steps to set up your development environment:

1. Install pipenv if you haven't already:

    ```bash 
    pip install pipenv
    ```
2. Clone the repository:

    ```bash 
    git clone https://github.com/your_username/django-country-kit.git
    ```
3. Navigate to the project directory:

    ```bash 
    cd django-country-kit
    ```
4. Install development dependencies:,

    ```bash 
    pipenv install --dev
    ```
5. Activate the virtual environment:

    ```bash 
    pipenv shell
    ```
6. Run migrations:

    ```bash 
    python manage.py migrate
    ```
7. Run collectstatic:

    ```bash 
    python manage.py collectstatic
    ```
8. Start the development server:

    ```bash 
    python manage.py runserver
    ```
