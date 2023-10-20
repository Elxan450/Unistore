from store.models import Category, ProductVersion, Manufacturer, Product
from django.http import JsonResponse
from .serializers import CategorySerializer, ProductSerializer, ManufacturerSerializer, ProductCommonSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter

class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="iexact")

    class Meta:
        model = Category
        fields = ()

class ProductFilter(filters.FilterSet):

    class Meta:
        model = ProductVersion
        fields = {
            "manufacturer": ['exact'],
            "price" : ['gt', 'lt']
        }


# @api_view(http_method_names=["GET", "POST"])
# def categories(request):
#     if request.method == "POST":
#         serializer = CategorySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, safe=False, status=201)
#         return JsonResponse(data=serializer.errors, safe=False, staus=400)
#     category_list = Category.objects.all()
#     serializer = CategorySerializer(category_list, many = True)
#     return JsonResponse(data=serializer.data, safe=False)

class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CategoryFilter

# @api_view(http_method_names=["PUT", "PATCH"])
# def category_update(request, id):
#     if request.method == "PUT":
#         category = Category.objects.get(id = id)
#         serializer = CategorySerializer(data = request.data, instance=category)
#         if serializer.is_valid():
#             return JsonResponse(data=serializer.data, safe=False, status=201)
#         return JsonResponse(data=serializer.errors, safe=False, staus=400)
#     category_list = Category.objects.all()
#     serializer = CategorySerializer(category_list, many = True)
#     return JsonResponse(data=serializer.data, safe=False)

class CategoryRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

# @api_view(http_method_names=["GET", "POST"])
# def products(request):
#     products_list = ProductVersion.objects.all()
#     serializer = ProductSerializer(products_list, context = {"request":request}, many = True)
#     return JsonResponse(data=serializer.data, safe=False)


class ProductsCommonAPIView(ListCreateAPIView):
    serializer_class = ProductCommonSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ("category", )

class ProductsAPIView(ListCreateAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductFilter
    # filterset_fields = ("manufacturer", )
    ordering_fields = ["price", "product"]
    
    

class ProductRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ProductVersion.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ManufacturerAPIView(ListCreateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )