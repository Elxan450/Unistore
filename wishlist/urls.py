from django.urls import path
from . import views

urlpatterns = [
    path('favorites/', views.favorites, name="favorites"),
    path('checkout/', views.checkout, name="checkout"),
    path('add_to_cart/<slug:slug>/', views.add_to_cart, name="add_to_cart"),
    path('remove_cart/<int:id>/', views.remove_cart, name="remove_cart"),
    path('add_quantity/<int:id>/', views.add_quantity, name="add_quantity"),
    path('sub_quantity/<int:id>/', views.sub_quantity, name="sub_quantity"), 

    path('add_to_fav/<slug:slug>/', views.add_to_fav, name="add_to_fav"),
    path('remove_fav/<slug:slug>/', views.remove_fav, name="remove_fav"),
]
