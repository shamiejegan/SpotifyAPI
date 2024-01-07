# DO NOT run this unless you would liek to clear all records from the database. 

import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append('')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify.settings')
django.setup()

from music.models import Track, Playlist, PlaylistTrack

# Delete all data from PlaylistTrack, Playlist, and Track models
PlaylistTrack.objects.all().delete()
Playlist.objects.all().delete()
Track.objects.all().delete()