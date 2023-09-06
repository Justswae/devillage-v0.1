from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Posts(models.Model):
    category = models.ForeignKey(Category, related_name= 'posts',default='', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post = models.TextField(max_length= 100000, blank = False)
    created_by = models.ForeignKey(User, related_name= 'posts' ,default= User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    