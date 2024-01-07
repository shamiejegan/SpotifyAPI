
from django.urls import path

from . import views 
from . import api

urlpatterns = [
    path('', views.index, name="index"),
    # web URLs 
    path('artists', views.artists, name='artists'),
    path('dance', views.dance, name='dance'),
    path('wordy', views.wordy, name='wordy'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('playlists', views.playlists, name='playlists'),
    # api URLs
    path('api/tracks/artist/<str:artist>', api.artist_tracks, name='artist'),
    path('api/tracks/dance/<int:n>', api.danceable_tracks, name='danceable_tracks'),
    path('api/tracks/wordy/<int:n>', api.wordy_tracks, name='wordy_tracks'),
    path('api/tracks/playlist/<str:playlist_id>', api.playlist_tracks, name='playlist_tracks'),
]
