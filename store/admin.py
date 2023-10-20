from django.contrib import admin
from .models import *

# Register your models here.

# class ProductInline(admin.TabularInline):


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(ProductImage)

admin.site.register(OperatingSystem)
admin.site.register(Display)
admin.site.register(Processor)
admin.site.register(Graphics)
admin.site.register(RAM)
admin.site.register(HardDrive)
admin.site.register(Wireless)
admin.site.register(PowerSupply)
admin.site.register(Battery)
admin.site.register(Manufacturer)

admin.site.register(Discount)

class ProductVersionInline(admin.TabularInline):
    model = ProductImage

@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ["id", "product"]
    inlines = [ProductVersionInline]
    list_display_links = ["id", "product"]


