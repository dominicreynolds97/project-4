from artists.serializers import ArtistSerializer
from django.db.models import fields
from rest_framework import serializers

from .models import Gig, Venue

class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = '__all__'
        
class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'

class PopulatedGigSerializer(GigSerializer):
    venue = VenueSerializer()
    support_artists = ArtistSerializer(many=True)
    headliner = ArtistSerializer()