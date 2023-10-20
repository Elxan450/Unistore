from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreListView.as_view(), name="store"),
    path('product/<str:slug>/', views.product, name="product"),
    path('product-review-edit/<str:slug>/', views.product_review_edit, name="product_review_edit"),
    path('product-review-delete/<str:slug>/', views.product_review_delete, name="product_review_delete"),
]
