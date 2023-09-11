from django.shortcuts import render
from authentication.models import SigninForm


def home(request):
    # replace css file pathname
    form = SigninForm()
    context = {'page_css': 'home.css', "form": form}
    return render(request, "home.html", context)
