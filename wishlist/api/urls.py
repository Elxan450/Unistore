from django.urls import path
from . import views

urlpatterns = [
    path("favorites/", views.FavoriteAPIView.as_view(), name="favorites"),
    path("favorite/<int:pk>/", views.FavoriteRetrieveUpdateDestroyAPIView.as_view()),
    path("cities/", views.CityAPIView.as_view()),
]
