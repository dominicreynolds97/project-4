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
    # def post(self, request, pk):
    #     try:
    #         artist = Artist.objects.get(pk=pk)
    #         if request.user in artist.favorited_by.all():
    #             artist.favorited_by.remove(request.user.id)
    #         else:
    #             artist.favorited_by.add(request.user.id)
    #         artist.save()
    #         serialized_artist = PopulatedArtistSerializer(artist)
    #         return Response(serialized_artist.data, status=status.HTTP_202_ACCEPTED)
    #     except Artist.DoesNotExist:
    #         raise NotFound()

class ReleaseFavoriteView(APIView):
    permission_classes = (IsAuthenticated, )
    def __init__(self):
        self.model = Release
        self.serial = PopulatedReleaseSerializer
    # permission_classes = (IsAuthenticated, )

    # def post(self, request, pk):
    #     try:
    #         release = Release.objects.get(pk=pk)
    #         if request.user in release.favorited_by.all():
    #             release.favorited_by.remove(request.user.id)
    #         else:
    #             release.favorited_by.add(request.user.id)
    #         release.save()
    #         serialized_release = PopulatedReleaseSerializer(release)
    #         return Response(serialized_release.data, status=status.HTTP_202_ACCEPTED)
    #     except Artist.DoesNotExist:
    #         raise NotFound()

class TrackFavoriteView(APIView):
    permission_classes = (IsAuthenticated, )
    def __init__(self):
        self.model = Track
        self.serial = PopulatedTrackSerializer
    # permission_classes = (IsAuthenticated, )

    # def post(self, request, pk):
    #     try:
    #         track = Track.objects.get(pk=pk)
    #         if request.user in track.favorited_by.all():
    #             track.favorited_by.remove(request.user.id)
    #         else:
    #             track.favorited_by.add(request.user.id)
    #         track.save()
    #         serialized_track = PopulatedTrackSerializer(track)
    #         return Response(serialized_track.data, status=status.HTTP_202_ACCEPTED)
    #     except Artist.DoesNotExist:
    #         raise NotFound()
