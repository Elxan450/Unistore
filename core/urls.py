from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('faq/', views.faq, name="faq"),
    path('export/', views.export_view, name="export"),

    #Paypal url
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-completed/', views.payment_completed_view, name="payment-completed"),
    path('payment-failed/', views.payment_failed_view, name="payment-failed"),
]
