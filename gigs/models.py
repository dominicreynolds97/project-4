from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from artists.models import Artist
from django.contrib.auth import get_user_model
User = get_user_model()
# from artists.models import Artists

# Create your models here.
class Venue(models.Model):
    name = CharField(max_length=100)
    description = TextField(max_length=500)
    location = TextField(max_length=200)
    favorited_by = ManyToManyField(
        User,
        related_name='favorite_venues',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

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
    headliner = ForeignKey(
        Artist,
        related_name='gig_headliner',
        on_delete=CASCADE
    )
    support_artists = ManyToManyField(
        Artist,
        related_name='gigs',
        blank=True
    )
    favorited_by = ManyToManyField(
        User,
        related_name='favorite_gigs',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'