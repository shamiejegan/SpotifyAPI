import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append('')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify.settings')
django.setup()

from music.models import * 

data_file = os.path.join(os.path.dirname(__file__), 'playlists.csv')

playlists = defaultdict(list)

with open(data_file, 'r', encoding='utf-8') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__() 
    for row in csv_reader: 
        playlists[row[0]] = row[1:4]
        
Playlist.objects.all().delete() 

for playlist_id, data in playlists.items(): 
    row = Playlist.objects.create(playlist_id=playlist_id, 
                              name=data[0], 
                              genre=data[1], 
                              )
    # perform database insertion 
    row.save()
