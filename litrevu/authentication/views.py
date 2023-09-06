from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from django.views.generic import View


class SigninView(View):
    template_name = "signin.html"
    form_class = models.SigninForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(
            request, self.template_name, context={
                "form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")
        message = "Identifiants invalides."
        return render(
            request, self.template_name, context={
                "form": form, "message": message}
        )


def render_signup_page(request):
    form = models.SignupForm()
    if request.method == "POST":
        form = models.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect("home")
    return render(request, "signup.html", context={"form": form, 'page_css': 'signup.css'})


def signout_user(request):
    logout(request)
    return redirect("home")
