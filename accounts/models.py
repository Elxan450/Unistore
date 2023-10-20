from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField("image", default="media/profile_images/default.jpg", upload_to = "profile_images/", null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.username}"
    
    