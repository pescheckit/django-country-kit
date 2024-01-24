"""
Module containing tests for country-related functionality in your Django app.

This module defines test classes for the 'Country', 'CountryField', and 'CountryWidget'
components in your Django app. It includes tests for the 'Country' class properties,
the 'CountryField' model field, and the 'CountryWidget' form widget.

Usage:
- Include this module in your Django app's 'tests' package.
- Run the tests using the Django test runner.

Example:
    # Run tests using the Django test runner:
    python manage.py test your_app.tests

Note:
    Make sure to set up the appropriate logging configuration and include this module
    in your project's tests configuration.

For more information, see Django documentation on testing:
https://docs.djangoproject.com/en/3.2/topics/testing/
"""

import logging

from django.db import models
from django.forms import ModelForm
from django.test import TestCase

from .fields import Country, CountryField
from .widgets import CountryWidget

logger = logging.getLogger(__name__)

class CountryTests(TestCase):
    """
    Test class for the 'Country' class.

    Methods:
        - test_country_name(): Test the name property of the Country class.
        - test_country_alpha3(): Test the alpha3 property of the Country class.
    """

    def test_country_name(self):
        """
        Test the name property of the Country class.
        """
        country = Country(code='US')
        self.assertEqual(country.name, 'United States')
        logger.info("test_country_name ✓")

    def test_country_alpha3(self):
        """
        Test the alpha3 property of the Country class.
        """
        country = Country(code='US')
        self.assertEqual(country.alpha3, 'USA')
        logger.info("test_country_alpha3 ✓")


class TestModel(models.Model):
    """
    A model with a CountryField.
    """

    country = CountryField()


class TestForm(ModelForm):
    """
    A form using the TestModel with CountryField.
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """ The model to use for the form."""
        model = TestModel
        fields = ['country']


class CountryFieldTests(TestCase):
    """
    Test class for the 'CountryField' model field.

    Methods:
        - test_country_field_max_length(): Test that max_length is set to 2 for CountryField.
        - test_country_field_choices(): Test that choices are populated from COUNTRIES.
    """

    def test_country_field_max_length(self):
        """
        Test that max_length is set to 2 for CountryField.
        """
        field = TestModel._meta.get_field('country')
        self.assertEqual(field.max_length, 2)
        logger.info("test_country_field_max_length ✓")

    def test_country_field_choices(self):
        """
        Test that choices are populated from COUNTRIES.
        """
        field = TestModel._meta.get_field('country')
        choices = field.choices
        self.assertEqual(len(choices), len(Country().countries_data))
        logger.info("test_country_field_choices ✓")


class CountryWidgetTests(TestCase):
    """
    Test class for the 'CountryWidget' form widget.

    Methods:
        - test_country_widget_choices(): Test that choices are populated from COUNTRIES for the widget.
    """

    def test_country_widget_choices(self):
        """
        Test that choices are populated from COUNTRIES for the widget.
        """
        widget = CountryWidget()
        choices = widget.choices
        self.assertEqual(len(choices), len(Country().countries_data))
        logger.info("test_country_widget_choices ✓")
