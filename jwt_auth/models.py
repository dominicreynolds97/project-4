from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField
# Create your models here.

class User(AbstractUser):
    email = CharField(max_length=50)
    avatar = CharField(
        max_length=300,
        default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_640.png'
    )
