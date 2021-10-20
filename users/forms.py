from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):

    email = forms.EmailField()
    passworld = forms.CharField(widget=PasswordInput)

    def clean_email(self):
        pass

    def clean_password(self):
        pass
    
