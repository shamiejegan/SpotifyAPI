import os
import sys
import django
import csv

sys.path.append('')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify.settings')
django.setup()

from music.models import *

data_file = os.path.join(os.path.dirname(__file__), 'playlisttrack.csv')

# Clear existing PlaylistTrack entries
PlaylistTrack.objects.all().delete()

# Create PlaylistTrack entries
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)

    for row in csv_reader:
        playlist_id = row[0]
        track_id = row[1]

        # Get playlist ids from existing Playlist table  
        playlist = Playlist.objects.get(playlist_id=playlist_id)
        # Get track ids from existing Track table  
        track = Track.objects.get(track_id=track_id)

        # because of unique constraint of table, only add the record if the foreign keys of track and playlist are unique. 
        playlist_track, created = PlaylistTrack.objects.get_or_create(
            playlist_id=playlist,
            track_id=track
        )

        # perform database insertion 
        playlist_track.save()

