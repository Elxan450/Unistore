from django.urls import path
from . import views

urlpatterns = [
    path("newsletters/", views.NewsletterAPIView.as_view(), name="newsletters")
]
