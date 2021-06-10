from django.contrib import admin
from artists.models import Artist, Track, Release, Musician, Genre, Instrument, Link

# Register your models here.
admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(Release)
admin.site.register(Musician)
admin.site.register(Genre)
admin.site.register(Instrument)
admin.site.register(Link)