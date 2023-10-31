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
    UserFollows.objects.get_or_create(user=request.user, followed_user=user_to_follow)
    # Django needs an http response
    return redirect("follow")


@login_required
def unfollow_user(request, user_id):
    UserModel = get_user_model()
    user_to_unfollow = get_object_or_404(UserModel, id=user_id)

    UserFollows.objects.filter(
        user=request.user, followed_user=user_to_unfollow
    ).delete()
    return redirect("follow")


@login_required
def find_user(request):
    UserModel = get_user_model()
    # Strip remove whitespaces before and after
    username = request.POST.get("username", "").strip()

    try:
        user_to_follow = UserModel.objects.get(username=username)

        # Prevent user from following themselve
        if user_to_follow == request.user:
            return follow(
                request, error_message="Vous ne pouvez pas vous abonner à vous-même."
            )

        # Check if already following
        elif UserFollows.objects.filter(
            user=request.user, followed_user=user_to_follow
        ).exists():
            return follow(
                request, error_message="Vous êtes déjà abonné à cet utilisateur"
            )

        else:
            UserFollows.objects.create(user=request.user, followed_user=user_to_follow)
            return follow(request, success_message=f"Vous suivez désormais {username}!")

    except UserModel.DoesNotExist:
        return follow(
            request,
            error_message=f"Aucun utilisateur du nom de '{username}' n'a été trouvé.",
        )


def follow(request, error_message="", success_message=""):
    UserModel = get_user_model()
    user_id = request.user.id
    user = get_object_or_404(UserModel, id=user_id)
    followings = user.following.all()  # Related name in models
    followers = user.followed_by.all()  # Related name in models

    return render(
        request,
        "follow.html",
        context={
            "css_files": ["follow.css"],
            "user": user,
            "success_message": success_message,
            "error_message": error_message,
            "followings": followings,
            "followers": followers,
        },
    )


def profile(request, user_id):
    UserModel = get_user_model()
    connected_user_id = request.user.id
    user = get_object_or_404(UserModel, id=user_id)
    connected_user = get_object_or_404(UserModel, id=connected_user_id)
    tickets = list(Ticket.objects.filter(user_id=user_id))
    reviews = list(Review.objects.filter(user_id=user_id))
    all_tickets_reviews = tickets + reviews
    sorted_by_most_recent = sorted(
        all_tickets_reviews, key=lambda x: x.time_created, reverse=True
    )

    return render(
        request,
        "profile.html",
        context={
            "css_files": ["feed.css"],
            "all_tickets_reviews": sorted_by_most_recent,
            "user": user,
            "connected_user": connected_user,
        },
    )
