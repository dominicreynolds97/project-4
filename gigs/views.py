from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Gig, Venue
from .serializers import GigSerializer,  VenueSerializer
# Create your views here.

class GigListView(APIView):
    def get(self, _request):
        gigs = Gig.objects.all()
        serialized_gigs = GigSerializer(gigs, many=True)
        return Response(serialized_gigs.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_gigs = GigSerializer(data=request.data)
        if serialized_gigs.is_valid():
            serialized_gigs.save()
            return Response(serialized_gigs.data, status=status.HTTP_201_CREATED)
        return Response(serialized_gigs.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class GigDetailView(APIView):
    def get_gig(self, pk):
        try:
            return Gig.objects.get(pk=pk)
        except Gig.DoesNotExist:
            raise NotFound()

    def get(self, _request, pk):
        gig = self.get_gig(pk=pk)
        serialized_gig = GigSerializer(gig)
        return Response(serialized_gig.data, status=status.HTTP_200_OK)
    
    def delete(self, _request, pk):
        gig = self.get_gig(pk=pk)
        gig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        gig = self.get_gig(pk=pk)
        updated_gig = GigSerializer(gig, data=request.data)
        if updated_gig.is_valid():
            updated_gig.save()
            return Response(updated_gig.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_gig.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class VenueListView(APIView):
    def get(self, _request):
        venue = Venue.objects.all()
        serialized_venue = VenueSerializer(venue, many=True)
        return Response(serialized_venue.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_venue = VenueSerializer(data=request.data)
        if serialized_venue.is_valid():
            serialized_venue.save()
            return Response(serialized_venue.data, status=status.HTTP_201_CREATED)
        return Response(serialized_venue.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class VenueDetailView(APIView):
    def get_venue(self, pk):
        try:
            return Venue.objects.get(pk=pk)
        except Venue.DoesNotExist:
            raise NotFound()

    def get(self, _request, pk):
        venue = self.get_venue(pk=pk)
        serialized_venue = VenueSerializer(venue)
        return Response(serialized_venue.data, status=status.HTTP_200_OK)
    
    def delete(self, _request, pk):
        venue = self.get_venue(pk=pk)
        venue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        venue = self.get_venue(pk=pk)
        updated_venue = VenueSerializer(venue, data=request.data)
        if updated_venue.is_valid():
            updated_venue.save()
            return Response(updated_venue.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_venue.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)