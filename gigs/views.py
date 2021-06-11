from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Gig, Venue
from .serializers import GigSerializer,  VenueSerializer
from hooks.views import ListView, DetailView
# Create your views here.

class GigListView(ListView):
    def __init__(self):
        self.model = Gig
        self.serial = GigSerializer

class GigDetailView(DetailView):
    def __init__(self):
        self.model = Gig
        self.serial = GigSerializer

class VenueListView(ListView):
    def __init__(self):
        self.model = Venue
        self.serial = VenueSerializer

class VenueDetailView(APIView):
    def __init__(self):
        self.model = Venue
        self.serial = VenueSerializer