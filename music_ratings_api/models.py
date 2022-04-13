from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    title = models.CharField(max_length=150)

    def __str__ (self):
      return f"{self.title}"


class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)

    def __str__ (self):
      return f"{self.title}"

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    duration = models.TimeField()

    ORDER_STATUS = (
        ('o', 'Side one'),
        ('t', 'Side two'),
        ('b', 'Bonus track'),
        ('e', 'Other'),
        )

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='0',
        help_text='Status',
        )

    def __str__ (self):
      album = self.album.title
      return f"{self.title} from {self.album}; ({self.duration})"

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

    def __str__ (self):
      user = self.user.name
      return f"{self.ratings} by {self.user}"

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)

    def __str__ (self):
      return f"{self.user}; {self.content}"

class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
