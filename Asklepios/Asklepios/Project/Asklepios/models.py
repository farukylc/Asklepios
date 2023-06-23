from django.db import models
from django.utils import timezone

# Create your models here.

class UploadImage(models.Model):

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    image = models.ImageField(default=None)
    result = models.CharField(max_length=20, default='Null')
    created_at = models.DateTimeField(default=timezone.now)

    
    
    
    