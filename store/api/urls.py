from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryAPIView.as_view(), name="categories"),
    path("category/<int:pk>/", views.CategoryRetriveUpdateDeleteAPIView.as_view(),
         name="category_update"),

    path("products/", views.ProductsAPIView.as_view(), name="products"),
    path("product/<int:pk>/", views.ProductRetriveUpdateDeleteAPIView.as_view(),
         name="products"),

     path("products_common/", views.ProductsCommonAPIView.as_view(), name="products_common"),
     

    path("manufacturers/", views.ManufacturerAPIView.as_view(), name="manufacturers"),
]
