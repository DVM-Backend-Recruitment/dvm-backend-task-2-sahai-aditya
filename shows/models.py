from django.db import models
from django.contrib.auth.models import User


class Theatre(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    total_seats = models.SmallIntegerField()
    cost_per_seat = models.SmallIntegerField()

class TheatreAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theatre = models.OneToOneField(Theatre, on_delete=models.CASCADE)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    image = models.ImageField(upload_to="movie-images/")