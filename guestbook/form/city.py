from django import forms
from django.core.exceptions import ValidationError

from guestbook.form import CustomForm


class CityForm(CustomForm):
    id = forms.IntegerField(required=False)
    name = forms.CharField()
    population = forms.IntegerField()
    gdp = forms.FloatField()
    schools = forms.MultipleChoiceField()

    def clean_schools(self):
        data = self.cleaned_data['schools']
        if len(data) == 0:
            raise ValidationError("School do not allow empty")
        return data
