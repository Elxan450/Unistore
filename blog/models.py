from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse

User = get_user_model()

# Create your models here.

class Blog(AbstractModel):
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description", max_length=10000)
    image = models.ImageField("Image", upload_to="blog_images/")
    slug = models.SlugField(null=True, blank=True, max_length=10000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("article", kwargs = {"slug":self.slug})
    
    class Meta:
        ordering = ["-created_at"]

class BlogReview(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_reviews")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_reviews")
    review = models.TextField("Review")
    slug = models.SlugField(null=True, blank=True, max_length=10000)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]


    def get_edit_url(self):
        return reverse_lazy("blog_review_edit", kwargs = {"slug":self.slug})
    
    def get_delete_url(self):
        return reverse_lazy("blog_review_delete", kwargs = {"slug":self.slug})
