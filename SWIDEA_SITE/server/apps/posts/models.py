from django.db import models

# Create your models here.

class Devtool(models.Model):
    name=models.CharField(max_length=50)
    kind=models.CharField(max_length=50)
    content=models.TextField()

class Idea(models.Model):
    title=models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE)

