from django.test import TestCase
from django.forms import ModelForm
from .fields import Country, CountryField
from .widgets import CountryWidget 
from django.db import models
import logging

logger = logging.getLogger(__name__)


class CountryTests(TestCase):
    def test_country_name(self):
        # Test the name property of the Country class
        country = Country(code='US')
        self.assertEqual(country.name, 'United States')
        logger.info("test_country_name ✓")

    def test_country_alpha3(self):
        # Test the alpha3 property of the Country class
        country = Country(code='US')
        self.assertEqual(country.alpha3, 'USA')
        logger.info("test_country_alpha3 ✓")

class TestModel(models.Model):
    # A model with a CountryField
    country = CountryField()

class TestForm(ModelForm):
    # A form using the TestModel with CountryField
    class Meta:
        model = TestModel
        fields = ['country']

class CountryFieldTests(TestCase):
    def test_country_field_max_length(self):
        # Test that max_length is set to 2 for CountryField
        field = TestModel._meta.get_field('country')
        self.assertEqual(field.max_length, 2)
        logger.info("test_country_field_max_length ✓")

    def test_country_field_choices(self):
        # Test that choices are populated from COUNTRIES
        field = TestModel._meta.get_field('country')
        choices = field.choices
        self.assertEqual(len(choices), len(Country().countries_data))
        logger.info("test_country_field_choices ✓")

class CountryWidgetTests(TestCase):
    def test_country_widget_choices(self):
        # Test that choices are populated from COUNTRIES for the widget
        widget = CountryWidget()
        choices = widget.choices
        self.assertEqual(len(choices), len(Country().countries_data))
        logger.info("test_country_widget_choices ✓")
