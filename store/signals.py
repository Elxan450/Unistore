from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import ProductVersion, ProductReview


@receiver(post_save, sender = ProductVersion)
def slug_create(sender, instance, created, *args, **kwargs):
    
    if created:
        instance.slug = slugify(instance.product.name) + str(instance.id)
        instance.save()

@receiver(post_save, sender = ProductReview)
def slug_create(sender, instance, created, *args, **kwargs):
    
    if created:
        instance.slug = slugify(instance.review) + str(instance.id)
        instance.save()
