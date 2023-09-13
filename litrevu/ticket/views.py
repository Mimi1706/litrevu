from django.shortcuts import render
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.


@login_required  # This decorator makes sure only logged user can create a ticket
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)  # Not immediately saving the form
            ticket.user = request.user  # Set the user from the request
            ticket.save()
            return redirect('feed')
    else:
        ticket_form = TicketForm()
    return render(request, 'ticket.html', {'ticket_form': ticket_form, "page_css": "form.css"})
