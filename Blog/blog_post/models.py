from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
     CHOICES = (
        ('1', 'title'),
        ('2', 'body'),
        ('3', 'author'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField(choices=CHOICES,default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Create your models here.
