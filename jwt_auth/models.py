from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from artists.models import Artist, Genre, Musician, Release, Track
# Create your models here.

class User(AbstractUser):
    email = CharField(max_length=50)
    avatar = CharField(max_length=300)