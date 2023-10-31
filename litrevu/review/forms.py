from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    is_edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    # class meta will use the Review model to create a form
    class Meta:
        model = Review
        fields = ['headline', 'body', 'rating']
