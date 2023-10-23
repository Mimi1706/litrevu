from django.shortcuts import render
from .forms import CreateReviewForm, EditReviewForm, Review
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import redirect, get_object_or_404


# Create your views here.


@login_required  # This decorator makes sure only logged user can create a review
def create_review(request):
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)  # Not immediately saving the form
            review.user = request.user  # Set the user from the request
            review.save()
            return redirect('feed')
    else:
        review_form = CreateReviewForm()
    return render(request, 'review.html', {'review_form': review_form, "css_files": ["form.css"]})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    form = EditReviewForm(instance=review)
    associated_ticket = review.ticket

    if request.method == 'POST' and 'edit_review' in request.POST:
        form = EditReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
        return redirect('posts')

    return render(request, 'edit_review.html', {
        'edit_review': form,
        "associated_ticket": associated_ticket,
        "css_files": ["form.css"]
    },)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()

    return redirect('posts')
