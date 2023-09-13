from django.shortcuts import render
from authentication.models import SigninForm


def home(request):
    signin_form = SigninForm()
    return render(request, "home.html", context={'page_css': 'home.css', "signin_form": signin_form})


def feed(request):
    return render(request, "feed.html", context={'page_css': 'feed.css'})
