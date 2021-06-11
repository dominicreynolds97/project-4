from artists.models import Track
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from artists.serializers import ArtistSerializer, ReleaseSerializer, GenreSerializer, TrackSerializer
from gigs.serializers import GigSerializer, VenueSerializer
User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    favorite_artists = ArtistSerializer(many=True)
    favorite_genres = GenreSerializer(many=True)
    favorite_releases = ReleaseSerializer(many=True)
    favorite_tracks = TrackSerializer(many=True)
    favorite_gigs = GigSerializer(many=True)
    favorite_venues = VenueSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email', 
            'favorite_artists', 
            'favorite_genres', 
            'favorite_releases', 
            'favorite_tracks',
            'favorite_gigs',
            'favorite_venues'
        )