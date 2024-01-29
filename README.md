# Django Country Kit

Django Country Kit is a Django app that provides country-related functionality, including a custom model field for storing country codes, a form widget for selecting countries, and associated tests.

## Features

- **Country Model Field:** Easily store and retrieve country codes in your Django models.
- **Country Widget:** A form widget for rendering a dropdown list of countries in your Django forms.
- **Tested:** Comprehensive tests for ensuring the functionality of the provided components.

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

3. Run migrations to create the necessary database tables:

    ```bash
    python manage.py migrate
    ```

4. Run collectstatic:

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

### Country Widget

In your forms, use the `CountryWidget` to render a dropdown list of countries:

```python
from django import forms
from django_country_kit.widgets import CountryWidget

class YourForm(forms.Form):
    country = forms.CharField(widget=CountryWidget())
```

### Custom settings

Django Country Kit provides custom settings for further customization of country data:

- `OVERRIDE_COUNTRIES`: Allows users to override specific countries with custom data.
- `EXCLUDE_COUNTRIES`: Allows users to exclude specific countries from the available choices.

You can customize these settings in your Django project's settings file to tailor the country data according to your needs.
