from django.shortcuts import render, redirect
from .forms import TicketForm

# Create your views here.


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        ticket_form = TicketForm()
    return render(request, 'ticket_form.html', {'ticket_form': ticket_form, "page_css": "ticket_form.css"})
