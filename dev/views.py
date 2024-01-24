from django.shortcuts import render
from django import forms
from django_country_kit.widgets import CountryWidget



class ExampleForm(forms.ModelForm):
    country = forms.ChoiceField(
        label='Your country',
        widget=CountryWidget(attrs={'class': 'form-control'}),
    )

    class Meta:
        fields = ('name', 'country')

# Create your views here.
def index(request):
    return render(request, 'dev/index.html', {"form": ExampleForm()})