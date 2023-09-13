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


urlpatterns = [
    path("", litrevu.views.home, name="home"),
    path('admin/', admin.site.urls),
    path("signin/", authentication.views.SigninView.as_view(), name="signin"),
    path("signup/", authentication.views.render_signup_page, name="signup"),
    path("signout/", authentication.views.signout_user, name="signout"),
    path("feed/", litrevu.views.feed, name="feed"),
    path("ticket/", ticket.views.create_ticket, name="ticket"),
    path("review/", review.views.create_review, name="review"),

]
