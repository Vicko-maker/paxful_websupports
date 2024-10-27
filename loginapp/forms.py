from django import forms
from .models import Person


class RegisterForm(forms.Form):
    class Meta:
        model = Person
        fields = ['email', 'username']
