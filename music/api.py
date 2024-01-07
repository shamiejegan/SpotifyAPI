from rest_framework.decorators import api_view #allow functions respond to different HTTP events
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import status

from .models import * 
from .serializers import * 
    
@api_view(['GET']) 
def artist_tracks(request, artist):
    if request.method =='GET': 
        # get tracks released by artist, ordered by descending order of release date (latest tracks will appear on top)
        tracks = Track.objects.all().filter(artist=artist).order_by('-release_date')
        if not tracks.exists():
            # if the artist name is not in the database, return a 404 error 
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

@api_view(['GET']) 
def danceable_tracks(request, n): 
    if request.method=='GET': 
        # get tracks in descending order of danceability index (highest value on top), filtering to only the top n records 
        tracks = Track.objects.all().order_by('-danceability')[:n]
        if not tracks.exists():
            # if no records are returned, return an empty array 
             return Response([])
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

@api_view(['GET']) 
def wordy_tracks(request, n): 
    if request.method=='GET': 
        # get tracks in descending order of wordiness index (highest value on top), filtering to only the top n records 
        tracks = Track.objects.all().order_by('-wordiness')[:n]
        if not tracks.exists():
            # if no records are returned, return an empty array 
             return Response([])
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
    
@api_view(['GET','POST']) 
def playlist_tracks(request, playlist_id):
    if request.method=='GET': 
        playlisttracks = PlaylistTrack.objects.all().filter(playlist_id=playlist_id)
        if not playlisttracks.exists():
            # if no records are returned, return a 404 error 
            return Response(status=status.HTTP_404_NOT_FOUND)
        # get a list of track ids within the specified playlist
        track_ids = [pt.track_id for pt in playlisttracks]
        # filter the track table to only include the tracks in the playlist and sort the tracks by popularity
        tracks = Track.objects.all().filter(name__in=track_ids).order_by('-popularity')
        if not tracks.exists():
            # if no records are returned, return a 404 error 
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        # get track id from the post
        track_id = request.data.get('track_id')
        # Check if the track with the given ID exists
        try:
            track = Track.objects.get(pk=track_id)
        except Track.DoesNotExist:
            return Response({'error': 'Track not found'}, status=status.HTTP_400_BAD_REQUEST)
        # check that the track does not already exist in the playlist 
        if PlaylistTrack.objects.filter(playlist_id=playlist_id, track_id=track_id).exists():
            return Response({'error': 'Track already exists in the playlist'}, status=status.HTTP_400_BAD_REQUEST)
        # Create a new PlaylistTrack instance
        playlist_track_data = {'playlist_id': playlist_id, 'track_id': track_id}
        serializer = PlaylistTrackSerializer(data=playlist_track_data)
        # save the record to the database if the data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
