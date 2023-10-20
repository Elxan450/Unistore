from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="blog"),
    path('<str:slug>/', views.article, name="article"),
    path('blog-review-edit/<str:slug>/', views.blog_review_edit, name="blog_review_edit"),
    path('blog-review-delete/<str:slug>/', views.blog_review_delete, name="blog_review_delete")
]