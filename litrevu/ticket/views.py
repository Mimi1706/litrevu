from django.shortcuts import render
from .forms import TicketForm
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404


# Create your views here.


@login_required  # This decorator makes sure only logged user can create a ticket
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)  # Not immediately saving the form
            ticket.user = request.user  # Set the user from the request
            ticket.save()
            return redirect('feed')
    else:
        ticket_form = TicketForm()
    return render(request, 'ticket.html', {'ticket_form': ticket_form, "page_css": "form.css"})


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    form = TicketForm(instance=ticket)

    if request.method == 'POST' and 'edit_ticket' in request.POST:
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
        return redirect('posts')

    return render(request, 'edit_ticket.html', {
        'edit_ticket': form,
        "page_css": "form.css"
    },)


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        ticket.delete()

    return redirect('posts')
