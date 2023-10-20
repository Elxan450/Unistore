from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Blog, BlogReview
from .forms import BlogReviewForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _

# Create your views here.

# def blog(request):
#     query = request.GET.get("search")
#     page = request.GET.get("page")

#     if query:
#         p = Paginator(Blog.objects.filter(title__icontains=query).order_by("-created_at"), 3)
#     else:
#         p = Paginator(Blog.objects.all().order_by("-created_at"), 3)
    
    
#     try:
#         blogs = p.page(page)
        
#     except PageNotAnInteger:
#         blogs = p.page(1)
         
#     except EmptyPage:
#         blogs = p.page(p.num_pages)


#     context = {
#         "blogs" : blogs,
#         "query" : query 
#     }

#     return render(request, "blog.html", context)


class BlogListView(ListView):
    template_name = "blog.html"
    model = Blog
    context_object_name = "blogs"
    paginate_by = 4


def article(request, slug):
    blog = get_object_or_404(Blog, slug = slug)
    form = BlogReviewForm()
    if request.method == "POST":
        form = BlogReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.blog = blog
            review.save()
            messages.success(request, "Successfuly sent!")
            return redirect(blog.get_absolute_url())
        else:
            messages.error(request, "Something went wrong, try again!")
            return redirect(blog.get_absolute_url())
        
    context = {
        "blog":blog, 
        "form":form,
    }
    return render(request, "article.html", context)


# class BlogDetailView(DetailView):
#     template_name = "article.html"
#     model = Blog

@login_required
def blog_review_edit(request, slug):
    review = get_object_or_404(BlogReview, slug = slug)
    blog = review.blog

    if request.user != review.user:
        messages.error(request, "You cannot access that page!")
        return redirect(blog.get_absolute_url())
        

    form = BlogReviewForm(instance=review)
    if request.method == "POST":
        form = BlogReviewForm(request.POST)
        if form.is_valid():
            review.review = form.cleaned_data["review"]
            review.edited = True
            review.save()
            messages.success(request, "Your review was edited successfully!")
            return redirect(blog.get_absolute_url())
        
        else:
            messages.error(request, "Invalid form!")
            return redirect(blog.get_absolute_url())
        
    context = {
        "form":form,
        "blog":blog
    }
    return render(request, "blog_review_edit.html", context)


@login_required
def blog_review_delete(request, slug):
    review = get_object_or_404(BlogReview, slug = slug)
    blog = review.blog

    if request.user != review.user:
        messages.error(request, "You cannot access that page!")
        return redirect(blog.get_absolute_url())

    if request.method == "POST" and request.user == review.user:
        review.delete()
        messages.success(request, "Your review was deleted successfully!")
        return redirect(blog.get_absolute_url())
        

    context = {
        "review":review,
        "blog":blog
    }

    return render(request, "blog_review_delete.html", context)

