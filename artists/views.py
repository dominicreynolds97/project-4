from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Track, Artist, Release
from .serializers import (
    ArtistSerializer,  
    ReleaseSerializer, 
    TrackSerializer, 
    PopulatedArtistSerializer,
    PopulatedTrackSerializer,
    PopulatedReleaseSerializer
)
from hooks.views import FavoriteView, ListView, DetailView

class TrackListView(ListView):
    def __init__(self):
        self.model = Track
        self.serial = TrackSerializer

class TrackDetailView(DetailView):
    def __init__(self):
        self.model = Track
        self.populated_serial = PopulatedTrackSerializer
        self.serial = TrackSerializer


class ArtistListView(ListView):
    def __init__(self):
        self.model = Artist
        self.serial = ArtistSerializer

class ArtistDetailView(DetailView):
    def __init__(self):
        self.model = Artist
        self.populated_serial = PopulatedArtistSerializer
        self.serial = ArtistSerializer

class ReleasesListView(ListView):
    def __init__(self):
        self.model = Release
        self.serial = ReleaseSerializer

class ReleaseDetailView(DetailView):
    def __init__(self):
        self.model = Release
        self.populated_serial = PopulatedReleaseSerializer
        self.serial = ReleaseSerializer

class ArtistFavoriteView(FavoriteView):

    permission_classes = (IsAuthenticated, )
    def __init__(self):
        self.model = Artist
        self.serial = PopulatedArtistSerializer

class ReleaseFavoriteView(FavoriteView):
    permission_classes = (IsAuthenticated, )
    def __init__(self):
        self.model = Release
        self.serial = PopulatedReleaseSerializer

class TrackFavoriteView(FavoriteView):
    permission_classes = (IsAuthenticated, )
    def __init__(self):
        self.model = Track
        self.serial = PopulatedTrackSerializer
