from artists.models import Release, Track
from gigs.models import Gig, Venue
from django.db.models.deletion import CASCADE
from jwt_auth.models import User
from django.db import models
from artists.models import Artist
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Comment(models.Model):
    content = models.TextField(max_length=250)
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    release = models.ForeignKey(
        Release,
        related_name='comments',
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    track = models.ForeignKey(
        Track,
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    gig = models.ForeignKey(
        Gig,
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    venue = models.ForeignKey(
        Venue,
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

