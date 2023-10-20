from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.db.models import Q

User = get_user_model()

# Create your models here.

# class Product(AbstractModel):

class Category(AbstractModel):
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField("Name", max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(AbstractModel):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    category = models.ForeignKey("category", on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name


class ProductReview(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_reviews")
    product_version = models.ForeignKey("ProductVersion", on_delete=models.CASCADE,  related_name="product_reviews", default=1)
    review = models.TextField("Review")
    slug = models.SlugField(null=True, blank=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return self.product_version.product.name
    
    def get_edit_url(self):
        return reverse_lazy("product_review_edit", kwargs = {"slug":self.slug})
    
    def get_delete_url(self):
        return reverse_lazy("product_review_delete", kwargs = {"slug":self.slug})

class ProductImage(AbstractModel):
    product_version = models.ForeignKey("ProductVersion", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Image", upload_to="product_images/")

    def __str__(self) -> str:
        return str(self.product_version.product.name)


#Product features
class OperatingSystem(AbstractModel):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name

class Display(AbstractModel):
    description = models.TextField("Description")

    def __str__(self):
        return self.description

class Processor(AbstractModel):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name


class Graphics(AbstractModel):
    description = models.TextField("Description")

    class Meta:
        verbose_name_plural = "Graphics"

    def __str__(self):
        return self.description

class RAM(AbstractModel):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name
    
class HardDrive(AbstractModel):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name

class Wireless(AbstractModel):
    description = models.TextField("Description")

    def __str__(self):
        return self.description

class PowerSupply(AbstractModel):
    name = models.CharField("Name", max_length=100)

    class Meta:
        verbose_name_plural = "Power supplies"

    def __str__(self):
        return self.name

class Battery(AbstractModel):
    name = models.CharField("Name", max_length=100)

    class Meta:
        verbose_name_plural = "Bateries"

    def __str__(self):
        return self.name

class Manufacturer(AbstractModel):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name

#ProductVersion
class ProductVersion(AbstractModel):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product_versions")
    operating_system = models.ForeignKey("OperatingSystem", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    display = models.ForeignKey("Display", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    processor = models.ForeignKey("Processor", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    graphics = models.ForeignKey("Graphics", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    ram = models.ForeignKey("RAM", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    hard_drive = models.ForeignKey("HardDrive", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    wireless = models.ForeignKey("Wireless", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    power_supply = models.ForeignKey("PowerSupply", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    battery = models.ForeignKey("Battery", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.SET_NULL, related_name="product_versions", null=True)
    price = models.FloatField("Price")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.product.name    
    
    def get_absolute_url(self):
        return reverse_lazy("product", kwargs = {"slug":self.slug})
    
    def get_discounted_price(self):

        try:
            discount = Discount.objects.get(Q(product=self), Q(is_active=True))
            discounted = self.price * (100 - discount.discount_percentage) / 100
            return discounted
        except:
            return False

    class Meta:
        ordering = ["-created_at"]

class Discount(AbstractModel):
    discount_percentage = models.FloatField("Discount in %")
    product = models.ForeignKey("ProductVersion", on_delete=models.CASCADE, related_name="discount")
    is_active = models.BooleanField("Active", default=False)

    def __str__(self):
        return self.product.product.name
    