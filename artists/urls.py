from django.urls import path
from .views import (
    ArtistListView,  
    TrackFavoriteView, 
    TrackListView, 
    ReleasesListView, 
    ArtistDetailView, 
    TrackDetailView, 
    ReleaseDetailView,
    ReleaseFavoriteView,
    ArtistFavoriteView
)

urlpatterns = [
    path('tracks/', TrackListView.as_view()),
    path('tracks/<int:pk>/', TrackDetailView.as_view()),
    path('tracks/<int:pk>/favorite/', TrackFavoriteView.as_view()),
    path('artists/', ArtistListView.as_view()),
    path('artists/<int:pk>/', ArtistDetailView.as_view()),
    path('artists/<int:pk>/favorite/', ArtistFavoriteView.as_view()),
    path('releases/', ReleasesListView.as_view()),
    path('releases/<int:pk>/', ReleaseDetailView.as_view()),
    path('releases/<int:pk>/favorite/', ReleaseFavoriteView.as_view()),
]