from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Blog, BlogReview
from django.utils.text import slugify

@receiver(post_save, sender = Blog)
def slug_create(sender, instance, created, *args, **kwargs):
    
    if created:
        instance.slug = slugify(instance.title) + str(instance.id)
        instance.save()

@receiver(post_save, sender = BlogReview)
def slug_create(sender, instance, created, *args, **kwargs):
    
    if created:
        instance.slug = slugify(instance.review) + str(instance.id)
        instance.save()
