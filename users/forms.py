from django import forms
from django.forms.widgets import PasswordInput
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                raise self.add_error(
                    "password", forms.ValidationError("Wrong password")
                )
        except models.User.DoesNotExist:
            raise self.add_error("email", forms.ValidationError("Email doesn't exist"))
