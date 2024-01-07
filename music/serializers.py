from rest_framework import serializers

from .models import * 

class TrackSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Track 
        # remove calculated quantitative metrics from what is visible to users, with the exception of duration
        fields = ['track_id','name','artist','release_date','duration_ms']

class PlaylistSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Playlist 
        # remove the id field from what is visible to users
        fields = ['name','genre']

class PlaylistTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistTrack
        fields = ['playlist_id', 'track_id']
