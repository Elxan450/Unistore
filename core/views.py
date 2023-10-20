from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _
from core.tasks import export_data  
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Your form was sent successfully!"))
            return redirect("contact")
        else:
            messages.error(request, _("Something went wrong!"))
            return redirect("contact")
        
    return render(request, "contact.html")

def about(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your form was sent successfully!")
            return redirect("about")
        else:
            messages.error(request, "Something went wrong!")
            return redirect("about")
        
    return render(request, "about.html")

def faq(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your form was sent successfully!")
            return redirect("faq")
        else:
            messages.error(request, "Something went wrong!")
            return redirect("faq")
        
    return render(request, "faq.html")


def export_view(request):
    export_data.delay()
    return HttpResponse("Success!")


def payment_completed_view(request):
    return render(request, "payment-completed.html")


def payment_failed_view(request):
    return render(request, "payment-failed.html")