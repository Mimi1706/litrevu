from django.shortcuts import render
from authentication.models import SigninForm
from ticket.models import Ticket
from review.models import Review


def home(request):
    signin_form = SigninForm()
    tickets = list(Ticket.objects.all())
    reviews = list(Review.objects.all())
    all_tickets_reviews = tickets + reviews
    sorted_by_most_recent = sorted(
        all_tickets_reviews, key=lambda x: x.time_created, reverse=True)
    return render(request, "home.html", context={'css_files': ['feed.css', 'home.css'], "signin_form": signin_form, 'all_tickets_reviews': sorted_by_most_recent})


def feed(request):
    # retrieve all followers and following of the user as QuerySets
    followed_relations = request.user.following.all()
    follower_relations = request.user.followed_by.all()

    # retrieve all the user instances
    followed_users = [
        relation.followed_user for relation in followed_relations]
    followers = [relation.user for relation in follower_relations]

    # converted to list() to be able to be concanated and set() to get rid of duplicates
    combined_users = list(set(followed_users + followers))
    tickets = list(Ticket.objects.filter(user__in=combined_users))
    reviews = list(Review.objects.filter(user__in=combined_users))

    # retrieve tickets and reviews of connected user
    user_tickets = list(Ticket.objects.filter(user=request.user))
    user_reviews = list(Review.objects.filter(user=request.user))
    tickets.extend(user_tickets)
    reviews.extend(user_reviews)

    # retrieve the reviews made in response to a ticket the connected user opened
    user_ticket_reviews = list(Review.objects.filter(ticket__in=user_tickets))
    reviews.extend(user_ticket_reviews)

    all_tickets_reviews = tickets + reviews
    sorted_by_most_recent = sorted(
        all_tickets_reviews, key=lambda x: x.time_created, reverse=True)

    return render(request, "feed.html", context={'css_files': ['feed.css'], 'all_tickets_reviews': sorted_by_most_recent})


def posts(request):
    tickets = list(Ticket.objects.filter(user=request.user.id))
    reviews = list(Review.objects.filter(user=request.user.id))
    all_tickets_reviews = tickets + reviews
    sorted_by_most_recent = sorted(
        all_tickets_reviews, key=lambda x: x.time_created, reverse=True)
    return render(request, "posts.html", context={'css_files': ['feed.css'], 'all_tickets_reviews': sorted_by_most_recent})
