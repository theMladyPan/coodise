from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import logout, login
from django.views import View
from ..forms.forms import LoginForm
from time import sleep
from django.urls import reverse
from django.contrib import messages


class Login(View):
    """Login webpage."""

    content = dict()
    template = "login.html"

    def get(self, request, *args, **kwargs):
        self.content["login_form"] = LoginForm
        return render(request, self.template, self.content)

    def post(self, request, *args, **kwargs):
        redirect_to = kwargs["redirect_to"]
        username = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        sleep(0.1)
        if user is None or not user.is_active:
            return render(request, self.template, self.content)
        login(request, user)
        messages.info(request, 'Logged in successfuly')
        return (
            redirect(reverse("path", args=(redirect_to,)))
            if redirect_to
            else redirect(reverse("index"))
        )


class Logout(View):
    """Logout webpage."""

    template = "login.html"
    content = dict()

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("index"))
