from django import forms
from guestbook.form import CustomForm


class CityForm(CustomForm):
    id = forms.IntegerField(required=False)
    name = forms.CharField(required=False)
    population = forms.IntegerField(required=False)
    gdp = forms.FloatField(required=False)
    schools = forms.IntegerField(required=False)
