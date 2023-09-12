from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=63, label="Identifiant", required="true")
    password = forms.CharField(
        max_length=63, widget=forms.PasswordInput, label="Mot de passe", required="true")


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username"]
