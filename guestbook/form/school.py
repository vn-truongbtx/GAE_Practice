from django import forms
from django.core.exceptions import ValidationError

from guestbook.form import CustomForm, ListField, BooleanFieldCustom


class SchoolForm(CustomForm):
    id = forms.IntegerField(required=False)
    name = forms.CharField(required=False)
    class_id = ListField(required=False)
    is_closed = BooleanFieldCustom(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data.startswith('school-'):
            raise ValidationError('School name must be same pattern school-*')
        return data

    def clean_class_id(self):
        data = self.cleaned_data.pop('class_id')
        for i in range(len(data)):
            try:
                data[i] = int(data[i])
            except ValueError as e:
                raise ValidationError('Class id must be integer')

        self.cleaned_data['class_id'] = data
        return data
