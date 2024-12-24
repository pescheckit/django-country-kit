"""
Module defining a Country class with internationalization support.

This module defines the 'Country' class, which represents a country with properties
for accessing its name and alpha3 code. It utilizes the 'get_countries' function
from the 'data' module to fetch country data.

Usage:
- Include this module in your Django app.

Example:
    # In your Django app's code:
    from .data import get_countries

    country = Country(code='US', custom_countries=get_countries())

Attributes:
    - Country (class): A class representing a country with properties for accessing its name and alpha3 code.
"""
from .data import get_countries
from .nationalities import NATIONALITIES


class Country:
    """
    A class representing a country with properties for accessing its name and alpha3 code.

    Attributes:
        - _countries_data (dict): A dictionary containing information about various countries.
        - _code (str): The country code.
    """

    def __init__(self, code=None, name=None, custom_countries=None):
        """
        Initialize a Country instance.

        Args:
            code (str): The country code.
            custom_countries (dict): Custom country data to use instead of fetching from get_countries().
        """
        if custom_countries:
            self._countries_data = custom_countries
        else:
            self._countries_data = get_countries()

        if name:
            self._code = self.get_code_from_name(name)
        elif code:
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
    def code(self) -> str:
        """Get the code of the country."""
        return self._code

    @property
    def alpha3(self) -> str:
        """Get the alpha3 code of the country."""
        return self._countries_data.get(self._code, {}).get('alpha3', '')

    def get_code_from_name(self, name: str) -> str:
        """
        Get the country code from the country name.

        Args:
            name (str): The name of the country.

        Returns:
            str: The country code.
        """
        for code, data in self._countries_data.items():
            if data['name'] == name:
                return code
        return ''

    def get_code_from_nationality(self, nationality: str) -> str:
        """
        Get the country code from the nationality.

        Args:
            nationality (str): The nationality of the country.

        Returns:
            str: The country code.
        """
        return NATIONALITIES.get(nationality, None)
