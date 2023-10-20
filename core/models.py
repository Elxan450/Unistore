from typing import Collection, Optional
from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbstractModel):
    message = models.TextField("Message")
    email = models.EmailField("Email", max_length=100)

    def __str__(self):
        return self.email

class Newsletter(AbstractModel):
    email = models.EmailField("Email", max_length=100, unique=True)

    def __str__(self):
        return self.email
    


    
