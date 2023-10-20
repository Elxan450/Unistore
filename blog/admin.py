from django.contrib import admin
from .models import Blog, BlogReview
from modeltranslation.admin import TranslationAdmin

# Register your models here.

# admin.site.register(Blog)
admin.site.register(BlogReview)


@admin.register(Blog)   
class BlogAdmin(TranslationAdmin):
    list_display =['title']