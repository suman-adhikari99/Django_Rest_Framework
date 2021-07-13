from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=40)
    

class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title



class Article(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
