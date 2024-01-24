from django.db import models
from .data import COUNTRIES

class Country:
    def __init__(self, code=None):
        self._countries_data = COUNTRIES
        self._code = code

    @property
    def countries_data(self):
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
    def __init__(self, *args, **kwargs):
        # Set max_length to 2 for country codes
        kwargs['max_length'] = 2
        # Use choices from the COUNTRIES data
        kwargs['choices'] = [(code, data['name']) for code, data in Country().countries_data.items()]
        super().__init__(*args, **kwargs)
