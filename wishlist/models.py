from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel
from store.models import ProductVersion
User = get_user_model()

# Create your models here.

# FavoriteList
class FavoriteList(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="fav_list")

    def __str__(self):
        return self.user.username
    
    def get_products(self):
        fav_model = self.products.all()
        products = []

        for model in fav_model:
            products.append(model.product)

        return products

class FavoriteListProduct(AbstractModel):
    favorite_list = models.ForeignKey(FavoriteList, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, related_name="fav_products")

    def __str__(self):
        return self.product.product.name
    


# CheckoutList
class CheckoutList(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="checkout_list")

    def __str__(self):
        return self.user.username
    
    def get_products(self):
        fav_model = self.checkout_products.filter(is_active=True)
        products = []

        for model in fav_model:
            products.append(model.product)

        return products

class CheckoutListProduct(AbstractModel):
    checkout_list = models.ForeignKey(CheckoutList, on_delete=models.CASCADE, related_name="checkout_products")
    product = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, related_name="checkout_products")
    quantity = models.IntegerField("Quantity", default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product.name
    


# CheckoutForm
class Country(AbstractModel):
    name = models.CharField("Country", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class City(AbstractModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField("City", max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"


class Checkout(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checkouts", null=True, blank=True)
    phone = models.CharField("Phone number", max_length=50)
    email = models.EmailField("E-mail", max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="checkouts", null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="checkouts", null=True, blank=True)
    street = models.CharField("Street", max_length=100)
    building = models.CharField("Building", max_length=50)
    zip = models.CharField("Zip", max_length=30)
    payment = models.CharField("Payment", max_length=50, null=True, blank=True)
    products = models.ManyToManyField(CheckoutListProduct)
    total_price = models.CharField("Total price", max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username
