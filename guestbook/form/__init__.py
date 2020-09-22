from django import forms


class CustomForm(forms.Form):
    def to_dict(self):
        ret = {}
        if not self.is_valid():
            return ret

        for field in self.fields:
            ret[field] = self.cleaned_data[field]
        return ret
