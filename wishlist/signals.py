from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import FavoriteList, CheckoutList
User = get_user_model()

@receiver(post_save, sender = User)
def fav_list_create(sender, instance, created, *args, **kwargs):
    if created:
        list = FavoriteList(user = instance)
        list.save()


@receiver(post_save, sender = User)
def checkout_list_create(sender, instance, created, *args, **kwargs):
    if created:
        list = CheckoutList(user = instance)
        list.save()
