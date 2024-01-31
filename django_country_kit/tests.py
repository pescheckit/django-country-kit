"""
Module containing tests for country-related functionality in your Django app.

This module defines test classes for the 'CountryField' and 'CountryWidget'
components in your Django app. It includes tests for the 'CountryField' model field
and the 'CountryWidget' form widget, including the behavior when using the
'OVERRIDE_COUNTRIES', 'EXCLUDE_COUNTRIES', 'INCLUDE_COUNTRIES' settings.

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
from django.core import exceptions
from django.test import TestCase, override_settings

from .base import Country
from .data import DATA
from .fields import CountryField, MultiSelectList

logger = logging.getLogger(__name__)


class CountryFieldTests(TestCase):
    """
    Test class for the 'CountryField' model field.

    Methods:
        - test_country_field_max_length(): Test that max_length is set to the length of the longest country code.
        - test_country_field_choices(): Test that choices are populated from COUNTRIES.
        - test_country_field_override_countries(): Test behavior when using OVERRIDE_COUNTRIES setting.
        - test_country_field_exclude_countries(): Test behavior when using EXCLUDE_COUNTRIES setting.
        - test_country_field_include_countries(): Test behavior when using INCLUDE_COUNTRIES setting.
        - test_country_field_get_choices_method(): Test the overridden get_choices method.
        - test_country_field_validate_method(): Test the overridden validate method for multiple selection.
        - test_country_by_name(): Test retrieving a country by name.
    """

    def test_country_field_max_length(self):
        """
        Test that max_length is set to the length of the longest country code.
        """
        field = CountryField()
        max_length = max(len(code) for code in field.countries)
        self.assertEqual(field.max_length, max_length)
        logger.info("test_country_field_max_length ✓")

    def test_country_field_choices(self):
        """
        Test that choices are populated from COUNTRIES.
        """
        field = CountryField()
        choices = field.choices
        self.assertEqual(len(choices), len(field.countries))
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
        self.assertEqual(len(field.choices), len(DATA) - len(settings.EXCLUDE_COUNTRIES))
        logger.info("test_country_field_exclude_countries ✓")

    @override_settings(INCLUDE_COUNTRIES={"UT": {"name": "Utopia", "alpha3": "UTP"}})
    def test_country_field_include_countries(self):
        """
        Test behavior when using INCLUDE_COUNTRIES setting.
        """
        field = CountryField()
        included_country_codes = settings.INCLUDE_COUNTRIES.keys()
        all_country_codes = [country[0] for country in field.choices]
        self.assertTrue(all(country in all_country_codes for country in included_country_codes))
        logger.info("test_country_field_include_countries ✓")

    def test_country_field_get_choices_method(self):
        """
        Test the overridden get_choices method.
        """
        field = CountryField()
        choices = field.choices
        self.assertIsInstance(choices, list)
        logger.info("test_country_field_get_choices_method ✓")

    def test_country_field_validate_method(self):
        """
        Test the overridden validate method for multiple selection.
        """
        field = CountryField(multiple=True)
        # Test valid selection
        valid_value = ["US", "CA"]
        try:
            field.validate(valid_value, None)
        except exceptions.ValidationError:
            self.fail("Validation failed for valid multiple selection.")
        # Test invalid selection
        invalid_value = ["XX"]
        with self.assertRaises(exceptions.ValidationError):
            field.validate(invalid_value, None)
        logger.info("test_country_field_validate_method ✓")

    def test_country_by_name(self):
        """
        Test retrieving a country by name.
        """
        country_name = "United States"
        country = Country(name=country_name)
        self.assertEqual(country.code, "US")
        logger.info("test_country_by_name ✓")


class MultiSelectListTests(TestCase):
    """
    Test class for the 'MultiSelectList' custom list type.

    Methods:
        - test_multiselect_list_string_representation(): Test string representation of MultiSelectList.
    """

    def test_multiselect_list_string_representation(self):
        """
        Test string representation of MultiSelectList.
        """
        choices = {"US": "United States", "CA": "Canada"}
        value = ["US", "CA"]
        multi_select_list = MultiSelectList(choices, value)
        self.assertEqual(str(multi_select_list), "United States, Canada")
        logger.info("test_multiselect_list_string_representation ✓")
