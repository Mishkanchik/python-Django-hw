from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser
from .utils import optimize_image
from django.conf import settings

class CustomUser(AbstractUser):
    image_small = models.ImageField(upload_to='users/', null=True, blank=True)
    image_large = models.ImageField(upload_to='users/', null=True, blank=True)
    image_medium = models.ImageField(upload_to='users/', null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    

    def __str__(self):
        return self.email 





class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title