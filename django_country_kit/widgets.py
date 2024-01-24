from django import forms
from .fields import Country

class CountryWidget(forms.Select):
    def __init__(self, attrs=None):
        # Ensure attrs is a dictionary
        attrs = attrs or {}
        
        # Use the superclass to initialize the widget
        super().__init__(attrs)

        # Populate choices based on COUNTRIES
        self.choices = [(code, data['name']) for code, data in Country().countries_data.items()]
