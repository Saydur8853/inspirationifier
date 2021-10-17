from django.db import models

# Create your models here.
class Image(models.Model):
    quotes = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=100000)
    
    def __str__(self):
        return self.quotes