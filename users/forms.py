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


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = {"first_name", "last_name", "email"}

    password = forms.CharField(widget=PasswordInput)
    password1 = forms.CharField(widget=PasswordInput, label="Password Repeat")

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation error")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)  # password encryption
        user.save()


# class SignUpForm(forms.Form):
#     first_name = forms.CharField(max_length=80)
#     last_name = forms.CharField(max_length=80)
#     email = forms.EmailField()
#     password = forms.CharField(widget=PasswordInput)
#     password1 = forms.CharField(widget=PasswordInput, label="Password Repeat")

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         try:
#             models.User.objects.get(email=email)
#             raise forms.ValidationError("User already exists")
#         except models.User.DoesNotExist:
#             return email

#     def clean_password1(self):
#         password = self.cleaned_data.get("password")
#         password1 = self.cleaned_data.get("password1")

#         if password != password1:
#             raise forms.ValidationError("Password confirmation error")
#         else:
#             return password

#     def save(self):
#         first_name = self.cleaned_data("first_name")
#         last_name = self.cleaned_data("last_name")
#         email = self.cleaned_data("email")
#         password = self.cleaned_data("password")
#         user = models.User.objects.create_user(email, email, password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
