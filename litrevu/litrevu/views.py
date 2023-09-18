from django.shortcuts import render
from authentication.models import SigninForm
from ticket.models import Ticket
from review.models import Review


def home(request):
    signin_form = SigninForm()
    return render(request, "home.html", context={'page_css': 'home.css', "signin_form": signin_form})


def feed(request):
    tickets = list(Ticket.objects.all())
    reviews = list(Review.objects.all())
    all_tickets_reviews = tickets + reviews
    sorted_by_most_recent = sorted(
        all_tickets_reviews, key=lambda x: x.time_created, reverse=True)
    return render(request, "feed.html", context={'page_css': 'card.css', 'all_tickets_reviews': sorted_by_most_recent})


def posts(request):
    tickets = list(Ticket.objects.filter(user=request.user.id))
    reviews = list(Review.objects.filter(user=request.user.id))
    all_tickets_reviews = tickets + reviews
    print(reviews[0].ticket.image)
    sorted_by_most_recent = sorted(
        all_tickets_reviews, key=lambda x: x.time_created, reverse=True)
    return render(request, "posts.html", context={'page_css': 'card.css', 'all_tickets_reviews': sorted_by_most_recent})
