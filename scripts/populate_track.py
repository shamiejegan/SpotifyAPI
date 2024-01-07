import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append('')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify.settings')
django.setup()

from music.models import * 

data_file = os.path.join(os.path.dirname(__file__), 'tracks.csv')

tracks = defaultdict(list)

with open(data_file) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__() 
    for row in csv_reader: 
        tracks[row[0]] = row[1:8]

Track.objects.all().delete() 

for track_id, data in tracks.items(): 
    row = Track.objects.create(track_id=track_id, 
                              name=data[0], 
                              artist=data[1], 
                              popularity=data[2], 
                              release_date=data[3], 
                              danceability= data[4], 
                              wordiness=data[5],
                              duration_ms=data[6]
                              )
    # perform database insertion 
    row.save()

