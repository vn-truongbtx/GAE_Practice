from django import forms
from django.core.exceptions import ValidationError
from django.utils import six


class CustomForm(forms.Form):
    def to_dict(self):
        ret = {}
        if self.errors:
            return ret

        for field, value in self.fields.items():
            if not value.required and not self.cleaned_data[field]:
                continue
            ret[field] = self.cleaned_data[field]
        return ret


class ListField(forms.MultipleChoiceField):
    def validate(self, value):
        if self.required and not value:
            raise ValidationError(self.error_messages['required'], code='required')


class BooleanFieldCustom(forms.BooleanField):
    def to_python(self, value):
        if isinstance(value, six.string_types) and value.lower() in ('false', '0'):
            value = False
        else:
            value = bool(value)
        return super(forms.BooleanField, self).to_python(value)
