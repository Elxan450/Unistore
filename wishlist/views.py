from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FavoriteList, FavoriteListProduct, Country, City, CheckoutListProduct
from store.models import ProductVersion
from django.views.generic import ListView
from .forms import CheckoutForm
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

@login_required
def favorites(request):
    user = request.user
    favorite_products = user.fav_list.products.all()

    context = {
        "favorite_products":favorite_products
    }

    return render(request, "favorites.html", context)


# class FavoriteListView(ListView):
#     template_name = "blog.html"
#     model = .fav_list.products.all()
#     context_object_name = "blogs"
#     paginate_by = 4


@login_required
def checkout(request):
    user = request.user
    checkout_products = user.checkout_list.checkout_products.filter(is_active=True)
    total_price = 0
    actual_price = 0

    for product in  checkout_products:  
        if product.product.get_discounted_price():
            total_price += product.product.get_discounted_price() * product.quantity
        else:
            total_price += product.product.price * product.quantity
        actual_price += product.product.price * product.quantity

    discount = actual_price - total_price
    discount = round(discount, 2)

    form = CheckoutForm()

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        country_name = request.POST.get("country")
        city_name = request.POST.get("city")
        country = Country.objects.get(name=country_name)
        city = City.objects.get(name=city_name)

        if form.is_valid(): 
            order = form.save(commit=False)                   
            order.user = user
            order.country = country
            order.city = city
            order.total_price = str(total_price)
            order.save()
            checkout_products = user.checkout_list.checkout_products.filter(is_active=True)
            if not checkout_products:
                messages.error(request, "You haven't chosen any products to order!")
                return redirect("store")

            for check in checkout_products:
                check.is_active = False
                check.save()
                order.products.add(check)
            order.save()
            messages.success(request, "Your order has been received !")
            return redirect("checkout")
        else:
            messages.error(request, "Fill form correctly !")
            return redirect("checkout")

    
    context = {
        "form" : form,
        "checkout_products" : checkout_products,
        "total_price" : total_price,
        "discount" : discount
    }

    return render(request, "checkout.html", context)


@login_required
def add_to_cart(request, slug):
    if request.method == "POST":        
        user = request.user
        product = get_object_or_404(ProductVersion, slug=slug)
        check = CheckoutListProduct.objects.filter(checkout_list = user.checkout_list, product = product, is_active=True)
        if not check:
            new_checkout = CheckoutListProduct(checkout_list=user.checkout_list, product=product)
            new_checkout.save()
            messages.success(request, "The product was added to your cart !")
            return redirect(reverse_lazy("product", kwargs={"slug":slug}))
        else:
            messages.info(request, "The product is already in your cart !")
            return redirect(reverse_lazy("product", kwargs={"slug":slug}))

    else:
        messages.error(request, "Something went wrong !")
        return redirect(reverse_lazy("product", kwargs={"slug":slug}))


@login_required
def remove_cart(request, id):
    user = request.user
    product = get_object_or_404(ProductVersion, id=id)
    check = CheckoutListProduct.objects.filter(checkout_list = user.checkout_list, product = product, is_active=True)
    if not check:
        messages.info(request, "The product was already removed!")
        return redirect("checkout")
    else:
        cur_checkout = CheckoutListProduct.objects.get(checkout_list=user.checkout_list, product=product, is_active=True)
        cur_checkout.delete()
        messages.success(request, "The product was removed !")
        return redirect("checkout")
    
@login_required
def add_quantity(request, id):
    user = request.user
    product = get_object_or_404(ProductVersion, id=id)
    try:
        check = CheckoutListProduct.objects.get(checkout_list = user.checkout_list, product = product, is_active=True)
        current = check.quantity
        check.quantity = current + 1
        check.save()
        return redirect("checkout")
    except:
        messages.error(request, "Something went wrong!")
        return redirect("checkout")

@login_required
def sub_quantity(request, id):
    user = request.user
    product = get_object_or_404(ProductVersion, id=id)
    try:
        check = CheckoutListProduct.objects.get(checkout_list = user.checkout_list, product = product, is_active=True)
        current = check.quantity
        if current == 1:
            messages.error(request, "Quantity cannot be zero!")
            return redirect("checkout")

        check.quantity = current - 1
        check.save()
        return redirect("checkout")
    except:
        messages.error(request, "Something went wrong!")
        return redirect("checkout")



@login_required
def add_to_fav(request, slug):
    try:        
        user = request.user
        product = get_object_or_404(ProductVersion, slug=slug)
        fav = FavoriteListProduct.objects.filter(favorite_list = user.fav_list, product = product)
        if not fav:
            new_fav = FavoriteListProduct(favorite_list=user.fav_list, product=product)
            new_fav.save()
            messages.success(request, "The product was added to your wishlist !")
            return redirect(reverse_lazy("product", kwargs={"slug" : slug}))
        else:
            messages.info(request, "The product is already in your wishlist !")
            return redirect(reverse_lazy("product", kwargs={"slug" : slug}))

    except:
        messages.error(request, "Something went wrong !")
        return redirect(reverse_lazy("product", kwargs={"slug" : slug}))


@login_required
def remove_fav(request, slug):
    user = request.user
    product = get_object_or_404(ProductVersion, slug=slug)
    check = FavoriteListProduct.objects.filter(favorite_list = user.fav_list, product = product)
    if not check:
        messages.info(request, "The product was already removed!")
        return redirect(reverse_lazy("product", kwargs={"slug" : slug}))
    else:
        cur_checkout = FavoriteListProduct.objects.get(favorite_list=user.fav_list, product=product)
        cur_checkout.delete()
        messages.success(request, "The product was removed from favorites!")
        return redirect(reverse_lazy("product", kwargs={"slug" : slug}))