import factory 
from random import randint, uniform, choice
from django.test import TestCase
from django.conf import settings 
from django.core.files import File 

from .models import * 

class TrackFactory(factory.django.DjangoModelFactory): 
    class Meta: 
        model = Track
    track_id = factory.Faker('uuid4')
    name = factory.Faker('word')
    artist = factory.Faker('name')
    popularity = randint(1,100)
    release_date = factory.Faker('date')
    danceability = round(uniform(0, 1), 2)
    wordiness = round(uniform(0, 1), 2)
    duration_ms = randint(30000,300000) #between 0.5 to 5 minutes in milliseconds 

class PlaylistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Playlist

    playlist_id = factory.Faker('uuid4')
    name = factory.Faker('word')
    genre = choice(['pop', 'rap', 'rock', 'latin', 'r&b','edm'])

class PlaylistTrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlaylistTrack

    playlist_id = factory.SubFactory(PlaylistFactory)
    track_id = factory.SubFactory(TrackFactory)
