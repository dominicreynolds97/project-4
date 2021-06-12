from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model, get_user_model

from .models import Genre, Musician, Track, Artist, Release
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class PopulatedArtistSerializer(ArtistSerializer):
    genres = GenreSerializer(many=True)
    musicians = MusicianSerializer(many=True)
    releases = ReleaseSerializer(many=True)
    favorited_by = UserSerializer(many=True)

class PopulatedReleaseSerializer(ReleaseSerializer):
    genres = GenreSerializer(many=True)
    favorited_by = UserSerializer(many=True)
    tracks = TrackSerializer(many=True)
    artist = ArtistSerializer()

class PopulatedTrackSerializer(TrackSerializer):
    genres = GenreSerializer(many=True)
    favorited_by = UserSerializer(many=True)