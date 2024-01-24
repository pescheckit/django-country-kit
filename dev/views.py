"""
Django Form and View for ExampleForm.

This module contains a Django Form class 'ExampleForm' and a view 'index'. The form includes
a custom 'country' field using Django Country Kit's 'CountryWidget' for handling country
information in the frontend.

Usage:
- Include this module in your Django app's forms.py and views.py files.
- Use the 'ExampleForm' in your views to render and process the form.

Example:
    # In your Django app's forms.py file:
    from django import forms
    from django_country_kit.widgets import CountryWidget

    class ExampleForm(forms.ModelForm):
        country = forms.ChoiceField(
            label='Your country',
            widget=CountryWidget(attrs={'class': 'form-control'}),
        )

        class Meta:
            fields = ('name', 'country')

    # In your Django app's views.py file:
    from django.shortcuts import render
    from .forms import ExampleForm

    def index(request):
        return render(request, 'dev/index.html', {"form": ExampleForm()})

Attributes:
    - ExampleForm (ModelForm): A Django ModelForm class representing the 'ExampleModel'.
    - index (function): A view function rendering the 'ExampleForm' in the 'dev/index.html' template.

Note:
    Make sure to include the 'CountryWidget' and 'ExampleForm' in your project's dependencies,
    and create the 'ExampleModel' model before using the 'ExampleForm'.

For more information, see Django documentation on forms and views:
https://docs.djangoproject.com/en/5/topics/forms/
https://docs.djangoproject.com/en/5/topics/http/views/
"""

from django import forms
from django.shortcuts import render

from django_country_kit.widgets import CountryWidget


class ExampleForm(forms.ModelForm):
    """
    Django ModelForm class for ExampleForm.

    Attributes:
        - country (ChoiceField): A choice field using 'CountryWidget' for handling country information.
    """

    country = forms.ChoiceField(
        label='Your country',
        widget=CountryWidget(attrs={'class': 'form-control'}),
    )

    class Meta:
        """Meta class for ExampleForm."""
        fields = ('name', 'country')


def index(request):
    """
    View function rendering the 'ExampleForm' in the 'dev/index.html' template.

    Parameters:
        - request (HttpRequest): The request object.

    Returns:
        - HttpResponse: The rendered response containing the 'ExampleForm'.
    """
    return render(request, 'dev/index.html', {"form": ExampleForm()})
