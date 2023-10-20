from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import NewsletterSerializer
from core.models import Newsletter

class NewsletterAPIView(ListCreateAPIView):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
