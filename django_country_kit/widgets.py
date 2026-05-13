"""
Module defining a Django form widget 'CountryWidget' with internationalization support.

This module defines the 'CountryWidget' class, a subclass of Django's 'Select' form widget.
It is designed for rendering a dropdown list of countries with internationalization support.

Usage:
- Include this module in your Django app.
- Use the 'CountryWidget' in your Django forms for rendering country selection.

Example:
    # In your Django app's forms.py file:
    from django import forms
    from .fields import Country
    from .widgets import CountryWidget

    class ExampleForm(forms.Form):
        country = forms.ChoiceField(widget=CountryWidget())

Attributes:
    - CountryWidget (class): A Django form widget for rendering a dropdown list of countries.
        It populates choices based on the 'COUNTRIES' data.

Note:
    Make sure to include this module in your project and set up internationalization in your Django app.

For more information, see Django documentation on forms and form widgets:
https://docs.djangoproject.com/en/5/topics/forms/
https://docs.djangoproject.com/en/5/ref/forms/widgets/
"""

from django import forms

from .base import Country


class CountrySelectMixin:
    """
    A mixin class to handle common functionalities for country select widgets.
    """

    def __init__(self, attrs=None, exclude=None, include=None):
        """
        Initialize the widget.

        Parameters:
            - attrs (dict): Additional attributes for the widget.
            - exclude (iterable): Country codes to exclude from the dropdown.
            - include (iterable): Country codes to restrict the dropdown to.
              When provided, only these codes (minus ``exclude``) are offered.
        """
        # Ensure attrs is a dictionary
        attrs = attrs or {}

        exclude = set(exclude or [])
        include = set(include or [])

        # Populate choices based on COUNTRIES, applying exclude/include filters
        self.choices = (
            (code, data['name'])
            for code, data in Country().countries_data.items()
            if code not in exclude and (not include or code in include)
        )

        # Use the superclass to initialize the widget
        super().__init__(attrs=attrs, choices=self.choices)


class CountryWidget(CountrySelectMixin, forms.Select):
    """
    A Django form widget for rendering a dropdown list of countries.
    """


class MultipleCountryWidget(CountrySelectMixin, forms.SelectMultiple):
    """
    A Django form widget for rendering a dropdown list of countries.
    """
