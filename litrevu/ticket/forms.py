from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    # class meta will use the Ticket model to create a form
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
