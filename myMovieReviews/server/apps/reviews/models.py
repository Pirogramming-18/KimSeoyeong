from django.db import models

# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=64)
    director=models.CharField(max_length=32)
    mainActor=models.TextField()
    genre=models.TextField()
    starRating=models.FloatField()
    runningTime=models.IntegerField()
    reviewContent=models.TextField()
    releaseYear=models.IntegerField()