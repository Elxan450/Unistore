from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductVersion, ProductReview
from .forms import ProductReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.

# def store(request):
#     product_versions = ProductVersion.objects.all()
#     context = {
#         "product_versions" : product_versions,
#     }

#     return render(request, "store.html", context)

class StoreListView(ListView):
    template_name = "store.html"
    model = ProductVersion
    context_object_name = "product_versions"
    paginate_by = 3

def product(request, slug):
    product_version = get_object_or_404(ProductVersion, slug=slug)
    form = ProductReviewForm()
     
    if request.method == "POST":
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            product_review = form.save(commit=False)
            product_review.user = request.user
            product_review.product_version = product_version
            product_review.save()
            messages.success(request, "Your comment was saved successfully!")
            return redirect(product_version.get_absolute_url())
                                                                
        else:
            messages.error(request, "Error has occurred!")
            return redirect(product_version.get_absolute_url())

    category = product_version.product.category
    
    all_products = ProductVersion.objects.all()
    related_products = []

    for product in all_products:
        if product.product.category == category and product.slug != slug:
            related_products.append(product)
    
    context = {
        "product_version":product_version, 
        "related_products":related_products,
        "form":form
    }

    return render(request, "product.html", context)


@login_required
def product_review_edit(request, slug):
    review = get_object_or_404(ProductReview, slug=slug)
    product_version = review.product_version

    if request.user != review.user:
        messages.error(request, "You cannot access that page!")
        return redirect(product_version.get_absolute_url())

    form = ProductReviewForm(instance=review)

    if request.method == "POST":
        form = ProductReviewForm(request.POST)

        if form.is_valid() and request.user == review.user:
            review.review = form.cleaned_data["review"]
            review.edited = True
            review.save()
            messages.success(request, "Your comment was changed successfully!")
            return redirect(product_version.get_absolute_url())

        else:
            messages.error(request, "Invalid form!")
            return redirect(product_version.get_absolute_url())

    context = {
        "product_version":product_version,
        "form":form,
    }

    return render(request, "product_review_edit.html", context)

@login_required
def product_review_delete(request, slug):
    review = get_object_or_404(ProductReview, slug=slug)
    product_version = review.product_version

    if request.user != review.user:
        messages.error(request, "You cannot access that page!")
        return redirect(product_version.get_absolute_url())

    if request.method == "POST":
        review.delete()
        messages.success(request, "Your review was deleted successfully!")
        return redirect(product_version.get_absolute_url())

    context = {
        "review":review,
        "product_version":product_version
    }

    return render(request, "product_review_delete.html", context)