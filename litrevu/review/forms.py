from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    is_edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    rating = forms.TypedChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        widget=forms.RadioSelect,
        coerce=int
    )

    # class meta will use the Review model to create a form
    class Meta:
        model = Review
        fields = ['headline', 'body', 'rating']
