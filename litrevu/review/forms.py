from django import forms
from .models import Review


class CreateReviewForm(forms.ModelForm):
    # class meta will use the Review model to create a form
    class Meta:
        model = Review
        fields = ['ticket', 'headline', 'body', 'rating']


class EditReviewForm(forms.ModelForm):
    # class meta will use the Review model to create a form
    class Meta:
        model = Review
        fields = ['headline', 'body', 'rating']
