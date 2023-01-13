from django.db import models

# Create your models here.
class Review(models.Model):

    GENRES = [
        ("action","액션"),
        ("comedy", "코미디"),
        ("sf","SF"),
        ("drama","드라마"),
        ("music","음악"),
        ("romance","로맨스"),
        ("history","역사"),
    ]

    title=models.CharField(max_length=64)
    director=models.CharField(max_length=32)
    mainActor=models.TextField()
    genre=models.TextField(max_length=32, choices=GENRES)
    starRating=models.FloatField()
    runningTime=models.IntegerField()
    reviewContent=models.TextField()
    releaseYear=models.IntegerField()