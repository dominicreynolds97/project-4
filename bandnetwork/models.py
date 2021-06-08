from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=50)
    length = models.PositiveIntegerField()
    urls = ArrayField(models.CharField(max_length=200))
    artist = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    members = ArrayField(models.CharField(max_length=50))
    genres = ArrayField(models.CharField(max_length=30))
    logo = models.CharField(max_length=300)
    cover_image = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    year_formed = models.IntegerField()

    def __str__(self):
        return self.name

class Release(models.Model):
    name = models.CharField(max_length=100)
    artist = models.IntegerField()
    tracks = ArrayField(models.IntegerField())
    release_date = models.DateField()
    urls = ArrayField(models.CharField(max_length=200))
    artwork = models.CharField(max_length=300)

    def __str__(self):
        return self.name

# class Venue(model.Models):

# class LiveShow(model.Models):