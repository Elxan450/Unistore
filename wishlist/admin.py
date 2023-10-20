from django.contrib import admin
from .models import FavoriteList, FavoriteListProduct,  Country, City, Checkout, CheckoutListProduct, CheckoutList

# Register your models here.

admin.site.register(FavoriteList)
admin.site.register(FavoriteListProduct)

admin.site.register(CheckoutList)
admin.site.register(CheckoutListProduct)

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Checkout)