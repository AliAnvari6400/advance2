from django.db import models
#from accounts.models import User
from django.contrib.auth import get_user_model
user = get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    # Create model for Post
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(blank=True,null=True)
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.title


