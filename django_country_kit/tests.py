"""
Module containing tests for country-related functionality in your Django app.

This module defines test classes for the 'CountryField' and 'CountryWidget'
components in your Django app. It includes tests for the 'CountryField' model field
and the 'CountryWidget' form widget, including the behavior when using the
'OVERRIDE_COUNTRIES' and 'EXCLUDE_COUNTRIES' settings.

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

from django.conf import settings
from django.test import TestCase, override_settings

from .fields import CountryField
from .widgets import CountryWidget

logger = logging.getLogger(__name__)


class CountryFieldTests(TestCase):
    """
    Test class for the 'CountryField' model field.

    Methods:
        - test_country_field_max_length(): Test that max_length is set to the length of the longest country code.
        - test_country_field_choices(): Test that choices are populated from COUNTRIES.
        - test_country_field_override_countries(): Test behavior when using OVERRIDE_COUNTRIES setting.
        - test_country_field_exclude_countries(): Test behavior when using EXCLUDE_COUNTRIES setting.
    """

    def test_country_field_max_length(self):
        """
        Test that max_length is set to the length of the longest country code.
        """
        field = CountryField()
        max_length = max(len(code) for code in field.countries_data)
        self.assertEqual(field.max_length, max_length)
        logger.info("test_country_field_max_length ✓")

    def test_country_field_choices(self):
        """
        Test that choices are populated from COUNTRIES.
        """
        field = CountryField()
        choices = field.choices
        self.assertEqual(len(choices), len(field.countries_data))
        logger.info("test_country_field_choices ✓")

    @override_settings(OVERRIDE_COUNTRIES={"US": {"name": "United States", "alpha3": "USA"}})
    def test_country_field_override_countries(self):
        """
        Test behavior when using OVERRIDE_COUNTRIES setting.
        """
        field = CountryField()
        self.assertEqual(len(field.choices), 1)
        logger.info("test_country_field_override_countries ✓")

    @override_settings(EXCLUDE_COUNTRIES=["US", "CA"])
    def test_country_field_exclude_countries(self):
        """
        Test behavior when using EXCLUDE_COUNTRIES setting.
        """
        field = CountryField()
        self.assertEqual(len(field.choices), len(field.countries_data) - len(settings.EXCLUDE_COUNTRIES))
        logger.info("test_country_field_exclude_countries ✓")


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
        choices = list(widget.choices)
        self.assertEqual(len(choices), len(widget.countries_data))
        logger.info("test_country_widget_choices ✓")
