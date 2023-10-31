from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, Review
from django.contrib.auth.decorators import login_required
from ticket.forms import TicketForm, Ticket


# Create your views here.


@login_required  # This decorator makes sure only logged user can create a review
def create_review(request, ticket_id):
    associated_ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            # Not immediately saving the form
            review = review_form.save(commit=False)
            review.user = request.user  # Set the user from the request
            review.ticket = associated_ticket  # Set the ticket from the request
            review.save()
            return redirect("feed")
    else:
        review_form = ReviewForm()

    return render(
        request,
        "review.html",
        {
            "associated_ticket": associated_ticket,
            "review_form": review_form,
            "css_files": ["form.css"],
        },
    )


@login_required
def create_ticket_and_review(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        # request.files for the image upload
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid() and review_form.is_valid():
            # Not immediately saving the form
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user  # Set the user from the request
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket  # link the review to the ticket
            review.user = request.user  # if the review model also has a user field
            review.save()

            return redirect("feed")
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return render(
        request,
        "ticket-and-review.html",
        {
            "ticket_form": ticket_form,
            "review_form": review_form,
            "css_files": ["form.css"],
        },
    )


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    associated_ticket = review.ticket
    form = ReviewForm(instance=review)

    if request.method == "POST" and "is_edit_review" in request.POST:
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
        return redirect("posts")

    return render(
        request,
        "edit_review.html",
        {
            "edit_review": form,
            "associated_ticket": associated_ticket,
            "css_files": ["form.css"],
        },
    )


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        review.delete()

    return redirect("posts")
