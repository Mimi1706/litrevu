from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import UserFollows
from ticket.models import Ticket
from review.models import Review


@login_required
def follow_user(request, user_id):
    UserModel = get_user_model()
    user_to_follow = get_object_or_404(UserModel, id=user_id)
    UserFollows.objects.get_or_create(
        user=request.user, followed_user=user_to_follow)
    # Django needs an http response
    return redirect("follow")


def follow(request):
    UserModel = get_user_model()
    user_id = request.user.id
    user = get_object_or_404(UserModel, id=user_id)
    following = user.following.all()  # Related name in models
    followers = user.followed_by.all()  # Related name in models

    return render(request, "follow.html", context={
        'file_css': 'follow.css',
        'user': user,
        'following': following,
        'followers': followers,
    })


def profile(request, user_id):
    UserModel = get_user_model()
    user = get_object_or_404(UserModel, id=user_id)
    tickets = list(Ticket.objects.filter(user_id=user_id))
    reviews = list(Review.objects.filter(user_id=user_id))
    all_tickets_reviews = tickets + reviews
    sorted_by_most_recent = sorted(
        all_tickets_reviews, key=lambda x: x.time_created, reverse=True)

    return render(request, "profile.html", context={
        'file_css': 'feed.css',
        'all_tickets_reviews': sorted_by_most_recent,
        'user': user,
    })
