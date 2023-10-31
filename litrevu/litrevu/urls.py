"""
URL configuration for litrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
import litrevu.views
import ticket.views
import review.views
import user.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", litrevu.views.home, name="home"),
    path("admin/", admin.site.urls),
    path("signin/", authentication.views.SigninView.as_view(), name="signin"),
    path("signup/", authentication.views.render_signup_page, name="signup"),
    path("signout/", authentication.views.signout_user, name="signout"),
    path("feed/", litrevu.views.feed, name="feed"),
    path("posts/", litrevu.views.posts, name="posts"),
    path("profile/<int:user_id>/", user.views.profile, name="profile"),
    path("follow/", user.views.follow, name="follow"),
    path("find-user/", user.views.find_user, name="find_user"),
    path("follow/<int:user_id>/", user.views.follow_user, name="follow_user"),
    path("unfollow/<int:user_id>/", user.views.unfollow_user, name="unfollow"),
    path("ticket/", ticket.views.create_ticket, name="ticket"),
    path("ticket/<int:ticket_id>/edit", ticket.views.edit_ticket, name="edit_ticket"),
    path(
        "ticket/<int:ticket_id>/delete/",
        ticket.views.delete_ticket,
        name="delete_ticket",
    ),
    path(
        "review/create-ticket-and-review",
        review.views.create_ticket_and_review,
        name="ticket-and-review",
    ),
    path(
        "review/ticket-<int:ticket_id>/create",
        review.views.create_review,
        name="review",
    ),
    path("review/<int:review_id>/edit", review.views.edit_review, name="edit_review"),
    path(
        "review/<int:review_id>/delete/",
        review.views.delete_review,
        name="delete_review",
    ),
]


# Only works in debug mode to display medias
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
