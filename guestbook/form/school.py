from django import forms
from django.core.exceptions import ValidationError

from guestbook.form import CustomForm


class SchoolForm(CustomForm):
    id = forms.IntegerField(required=False)
    name = forms.CharField()
    class_id = forms.MultipleChoiceField()
    is_closed = forms.BooleanField()

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data.startswith('school-'):
            raise ValidationError('School name is not valid')
