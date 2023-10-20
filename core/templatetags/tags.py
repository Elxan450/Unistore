from django.template import Library
from store.models import Category
from core.forms import ContactForm
from blog.forms import BlogReviewForm
from blog.models import Blog
from store.models import Manufacturer, ProductVersion, Product, Category
from wishlist.models import Country, City

register = Library()

@register.simple_tag
def get_categories(limit = 3):
    return Category.objects.all()[:limit]

@register.simple_tag
def get_all_categories():
    return Category.objects.all()

@register.simple_tag
def get_all_manufacturers():
    return Manufacturer.objects.all()

@register.simple_tag
def get_blogs(limit = 2):
    return Blog.objects.all()[:limit]

@register.simple_tag
def contact_form():
    form = ContactForm()
    return form

@register.simple_tag
def countries():
    return Country.objects.all()

@register.simple_tag
def cities():
    return City.objects.all()


@register.simple_tag
def tablets():
    res = []
    try:
        category = Category.objects.get(name = "Tablet")
        products = Product.objects.filter(category = category)
        for i in range(3):
            product_versions = ProductVersion.objects.filter(product = products[i])
            res.append(product_versions[0])

        return res
    
    except:
        return res


@register.simple_tag
def desktops():
    res = []
    try:
        category = Category.objects.get(name = "Desktop")
        products = Product.objects.filter(category = category)
        for i in range(3):
            product_versions = ProductVersion.objects.filter(product = products[i])
            res.append(product_versions[0])

        return res
    
    except:
        return res


@register.simple_tag
def hybrids():
    res = []
    try:
        category = Category.objects.get(name = "Hybrid")
        products = Product.objects.filter(category = category)
        for i in range(3):
            product_versions = ProductVersion.objects.filter(product = products[i])
            res.append(product_versions[0])

        return res
    
    except:
        return res
