from blog.models import Blog
from .serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter

class BlogAPIView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    ordering_fields = ["title"]
    # permission_classes = (IsAuthenticatedOrReadOnly,)
