from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from artists.models import Artist
# from artists.models import Artists

# Create your models here.
class Venue(models.Model):
    name = CharField(max_length=100)
    description = TextField(max_length=500)
    location = TextField(max_length=200)

class Gig(models.Model):
    name = CharField(max_length=150)
    description = TextField(max_length=500)
    date_time = DateTimeField()
    price = CharField(max_length=10)
    venue = ForeignKey(
        Venue,
        related_name='gigs',
        on_delete=CASCADE
    )
    artists = ManyToManyField(
        Artist,
        related_name='gigs',
        blank=True
    )