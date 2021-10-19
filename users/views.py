from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", context={"form": form})

    def post(self, request):
        pass
