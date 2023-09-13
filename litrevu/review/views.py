from django.shortcuts import render
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.


@login_required  # This decorator makes sure only logged user can create a ticket
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)  # Not immediately saving the form
            ticket.user = request.user  # Set the user from the request
            ticket.save()
            return redirect('feed')
    else:
        review_form = ReviewForm()
    return render(request, 'review.html', {'review_form': review_form, "page_css": "form.css"})
