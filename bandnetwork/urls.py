from bandnetwork.serializers import ReleaseSerializer
from django.urls import path
from .views import ArtistListView, TrackListView, ReleasesListView, ArtistDetailView, TrackDetailView, ReleaseDetailView

urlpatterns = [
    path('tracks/', TrackListView.as_view()),
    path('tracks/<int:pk>/', TrackDetailView.as_view()),
    path('artists/', ArtistListView.as_view()),
    path('artists/<int:pk>/', ArtistDetailView.as_view()),
    path('releases/', ReleasesListView.as_view()),
    path('releases/<int:pk>/', ReleaseDetailView.as_view())
]