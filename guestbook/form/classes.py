from django import forms

from guestbook.form import CustomForm


class ClassForm(CustomForm):
    id = forms.IntegerField(required=False)
    name = forms.CharField()
    number_of_student = forms.IntegerField()