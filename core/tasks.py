import time
from celery import shared_task  
from django.template.loader import render_to_string
from core.models import Newsletter
from blog.models import Blog    
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@shared_task
def export_data():
    print("Export start...")
    time.sleep(10)
    print("Export end...")


@shared_task
def sene_email_to_subsribers():
    email_list = Newsletter.objects.values_list("email", flat=True)
    blogs = Blog.objects.all()[:3]
    subject = "Latest posts"
    message = render_to_string("email-subscribers.html", {
        "blogs" : blogs,    
    })

    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = "HTML"
    mail.send()