from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
     CHOICES = (
        ('sun', 'sunday'),
        ('mon', 'monday'),
        ('tue', 'tuesday'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField(choices=CHOICES,default='mon')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Create your models here.
