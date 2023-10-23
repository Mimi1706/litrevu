from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from django.views.generic import View


class SigninView(View):
    template_name = "signin.html"
    signin_form_model = models.SigninForm

    def post(self, request):
        signin_form = self.signin_form_model(request.POST)
        if signin_form.is_valid():  # if the fields are valid
            user = authenticate(
                username=signin_form.cleaned_data["username"],
                password=signin_form.cleaned_data["password"],
            )
            if user is not None:  # if a user is found
                login(request, user)
                return redirect("home")
            else:
                message = 'Identifiants invalides.'
        return render(
            request, "home.html", context={
                "signin_form": signin_form, 'message': message, 'css_files': ['home.css']}
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
    return render(request, "signup.html", context={"form": form, 'css_files': ['signup.css']})


def signout_user(request):
    logout(request)
    return redirect("home")
