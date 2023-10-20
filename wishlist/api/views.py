from wishlist.models import FavoriteList, FavoriteListProduct, City
from .serializers import FavoriteListProductSerializer, CitySerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters

class FavoriteAPIView(ListCreateAPIView):
    serializer_class = FavoriteListProductSerializer
    queryset = FavoriteListProduct.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ("favorite_list", "product")
    # permission_classes = (IsAuthenticatedOrReadOnly,)

class FavoriteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FavoriteListProductSerializer
    queryset = FavoriteListProduct.objects.all()


class CityAPIView(ListCreateAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ("country", )
    # permission_classes = (IsAuthenticatedOrReadOnly,)