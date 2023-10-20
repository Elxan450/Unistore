from rest_framework import serializers
from store.models import Category, ProductVersion, ProductImage, Manufacturer, Product


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            "id", 
            "name",
        )

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = (
            "id",
            "name"
        )

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = (
            "id", 
            "image",
        )



class ProductSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source = "product.name")
    description = serializers.CharField(source = "product.description")
    category = serializers.CharField(source = "product.category.name")
    operating_system = serializers.CharField(source = "operating_system.name")
    display = serializers.CharField(source = "display.description")
    processor = serializers.CharField(source = "processor.name")
    graphics = serializers.CharField(source = "graphics.description")
    ram = serializers.CharField(source = "ram.name")
    hard_drive = serializers.CharField(source = "hard_drive.name")
    wireless = serializers.CharField(source = "wireless.description")
    power_supply = serializers.CharField(source = "power_supply.name")
    battery = serializers.CharField(source = "battery.name")
    manufacturer = serializers.CharField(source = "manufacturer.name")
    images = ImageSerializer(many = True)


    class Meta:
        model = ProductVersion
        fields = (
            "id",
            "product", 
            "description",
            "category",
            "operating_system",
            "display", 
            "processor",
            "graphics",
            "ram",
            "hard_drive",
            "wireless",
            "power_supply",
            "battery",
            "manufacturer",
            "images",
            "price",
            "get_discounted_price",
            "slug"
        )


class ProductCommonSerializer(serializers.ModelSerializer):

    product_versions = ProductSerializer(many = True)

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "category",
            "product_versions"
        )