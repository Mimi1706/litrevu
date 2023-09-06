from django.shortcuts import render


def home(request):
    # replace css file pathname
    context = {'page_css': 'home.css'}
    return render(request, "home.html", context)
