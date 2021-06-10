from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Track, Artist, Release
from .serializers import ArtistSerializer,  ReleaseSerializer, TrackSerializer
# Create your views here.

class TrackListView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        tracks = Track.objects.all()
        serialized_tracks = TrackSerializer(tracks, many=True)
        return Response(serialized_tracks.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_tracks = TrackSerializer(data=request.data)
        if serialized_tracks.is_valid():
            serialized_tracks.save()
            return Response(serialized_tracks.data, status=status.HTTP_201_CREATED)
        return Response(serialized_tracks.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class TrackDetailView(APIView):
    def get_track(self, pk):
        try:
            return Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            raise NotFound()

    def get(self, _request, pk):
        track = self.get_track(pk=pk)
        serialized_track = TrackSerializer(track)
        return Response(serialized_track.data, status=status.HTTP_200_OK)
    
    def delete(self, _request, pk):
        track = self.get_track(pk=pk)
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        track = self.get_track(pk=pk)
        updated_track = TrackSerializer(track, data=request.data)
        if updated_track.is_valid():
            updated_track.save()
            return Response(updated_track.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_track.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ArtistListView(APIView):
    def get(self, _request):
        artists = Artist.objects.all()
        serialized_artists = ArtistSerializer(artists, many=True)
        return Response(serialized_artists.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_artists = ArtistSerializer(data=request.data)
        if serialized_artists.is_valid():
            serialized_artists.save()
            return Response(serialized_artists.data, status=status.HTTP_201_CREATED)
        return Response(serialized_artists.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ArtistDetailView(APIView):
    def get_artist(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise NotFound()

    def get(self, _request, pk):
        artist = self.get_artist(pk=pk)
        serialized_artist = ArtistSerializer(artist)
        return Response(serialized_artist.data, status=status.HTTP_200_OK)

    def delete(self, _request, pk):
        artist = self.get_artist(pk=pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        artist = self.get_artist(pk=pk)
        updated_artist = ArtistSerializer(artist, data=request.data)
        if updated_artist.is_valid():
            updated_artist.save()
            return Response(updated_artist.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_artist.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ReleasesListView(APIView):
    def get(self, _response):
        releases = Release.objects.all()
        serialized_releases = ReleaseSerializer(releases, many=True)
        return Response(serialized_releases.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_release = ReleaseSerializer(data=request.data)
        if serialized_release.is_valid():
            serialized_release.save()
            return Response(serialized_release.data, status=status.HTTP_201_CREATED)
        return Response(serialized_release.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ReleaseDetailView(APIView):
    def get_release(self, pk):
        try:
            return Release.objects.get(pk=pk)
        except Release.DoesNotExist:
            raise NotFound()

    def get(self, _response, pk):
        release = self.get_release(pk=pk)
        serialized_release = ReleaseSerializer(release)
        return Response(serialized_release, status=status.HTTP_200_OK)

    def delete(self, _request, pk):
        release = self.get_release(pk=pk)
        release.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        release = self.get_releaset(pk=pk)
        updated_release = ReleaseSerializer(release, data=request.data)
        if updated_release.is_valid():
            updated_release.save()
            return Response(updated_release.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_release.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)