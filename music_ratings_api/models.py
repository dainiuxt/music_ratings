from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    title = models.CharField(max_length=150)


class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    duration = models.TimeField()

class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    ratings = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)

class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
