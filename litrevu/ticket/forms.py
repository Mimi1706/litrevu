from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    # forms.HiddenInput hides this element from the frontend
    # directly set to true when modifiying the ticket
    is_edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    # class meta will use the Ticket model to create a form
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {
            "title": "Titre",
            "description": "Description",
        }
