from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import serializers, status
from .models import Track, Artist, Release
from .serializers import ArtistSerializer, ReleaseSerializer, TrackSerializer

# Create your views here.
class TrackListView(APIView):
    def get(self, _request):
        tracks = Track.objects.all()
        serialized_tracks = TrackSerializer(tracks, many=True)
        return Response(serialized_tracks.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_tracks = TrackSerializer(data=request.data)
        print(request.data)
        if serialized_tracks.is_valid():
            serialized_tracks.save()
            return Response(serialized_tracks.data, status=status.HTTP_201_CREATED)
        return Response(serialized_tracks.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class TrackDetailView(APIView):
    def get(self, _request, pk):
        try:
            track = Track.objects.get(pk=pk)
            serialized_track = TrackSerializer(track)
            return Response(serialized_track.data, status=status.HTTP_200_OK)
        except Track.DoesNotExist:
            raise NotFound()


class ArtistListView(APIView):
    def get(self, _request):
        artists = Artist.objects.all()
        serialized_artists = ArtistSerializer(artists, many=True)
        return Response(serialized_artists.data, status=status.HTTP_200_OK)

class ArtistDetailView(APIView):
    def get(self, _request, pk):
        try:
            artist = Artist.objects.get(pk=pk)
            serialized_artist = ArtistSerializer(artist)
            return Response(serialized_artist.data, status=status.HTTP_200_OK)
        except Artist.DoesNotExist:
            raise NotFound()

class ReleasesListView(APIView):
    def get(self, _response):
        releases = Release.objects.all()
        serialized_releases = ReleaseSerializer(releases, many=True)
        return Response(serialized_releases.data, status=status.HTTP_200_OK)

class ReleaseDetailView(APIView):
    def get(self, _response, pk):
        try:
            release = Release.objects.get(pk=pk)
            serialized_release = ReleaseSerializer(release)
            return Response(serialized_release, status=status.HTTP_200_OK)
        except Release.DoesNotExist:
            raise NotFound()