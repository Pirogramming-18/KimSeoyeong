from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=150)
    like = models.BooleanField(default=False)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.CharField(max_length=150)