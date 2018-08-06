from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import logout, login
from django.views import View
from ..forms.forms import LoginForm

class Login(View):
    content = dict()
    template = "login.html"

    def get(self, request, *args, **kwargs):
        self.content["form"] = LoginForm
        return render(request, self.template, self.content)

    def post(self, request, *args, **kwargs):
        redirect_to = kwargs["redirect_to"]
        if redirect_to != "":
            redirect_to = "path/" + redirect_to

        username = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/" + redirect_to)
        else:
            return render(request, self.template, self.content)

class Logout(View):
    template = "login.html"
    content = dict()
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")

        return render(request, self.template, self.content)
