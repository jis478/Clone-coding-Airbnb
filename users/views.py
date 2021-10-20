from django.shortcuts import render
from django.views import View
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "marksk82@gmail.com"})
        return render(request, "users/login.html", context={"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        return render(request, "users/login.html", context={"form": form})
