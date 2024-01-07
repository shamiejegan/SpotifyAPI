from django.test import TestCase

import json 
from django.urls import reverse 
from rest_framework.test import APITestCase

from .model_factories import * 
from .serializers import * 

# Create your tests here.
class APITests(APITestCase): 
    def setUp(self):
        # Create tracks, playlists, and playlist tracks for testing
        track = TrackFactory.create(pk='JF03M5KFL6L9L1NBJ2JM4T', artist='Shamie')
        playlist = PlaylistFactory.create(pk='CD9002MLF9D9ISJ3I4KC5Y')
        PlaylistTrackFactory.create(track_id=track, playlist_id=playlist)
        self.good_artist_url= reverse('artist', kwargs={'artist': 'Shamie'})
        self.bad_artist_url= reverse('artist', kwargs={'artist': 'ABC'})
        self.good_dance_url= reverse('danceable_tracks', kwargs={'n': 5})
        self.good_wordy_url= reverse('wordy_tracks', kwargs={'n': 5})
        self.good_playlist_url = reverse('playlist_tracks', kwargs={'playlist_id': 'CD9002MLF9D9ISJ3I4KC5Y'})
        self.bad_playlist_url = reverse('playlist_tracks', kwargs={'playlist_id': '0'})
        self.post_playlisttrack_url=reverse('playlist_tracks', kwargs={'playlist_id': 'CD9002MLF9D9ISJ3I4KC5Y'})

    def tearDown(self):
        # remove all the records that were added to the database after test is run 
        Track.objects.all().delete()
        Playlist.objects.all().delete()
        PlaylistTrack.objects.all().delete() 
    
    # test API response status codes 
    def test_trackArtistReturnSuccess(self): 
        # create an entry into track with the artist value "Shamie". The artist API should return a 200 status with Shamie 
        response = self.client.get(self.good_artist_url, format='json')
        response.render() 
        self.assertEqual(response.status_code,200)
    def test_trackArtistReturn404(self): 
        # create an entry into track with the artist value "Shamie". The artist API should return a 200 status with Shamie 
        response = self.client.get(self.bad_artist_url, format='json')
        response.render() 
        self.assertEqual(response.status_code,404)
    def test_trackDanceReturnSuccess(self): 
        # The dance API should return a 200 status with input of an integer 
        response = self.client.get(self.good_dance_url, format='json')
        response.render() 
        self.assertEqual(response.status_code,200)
    def test_trackWordReturnSuccess(self): 
        # The wordy API should return a 200 status with input of an integer  
        response = self.client.get(self.good_wordy_url, format='json')
        response.render() 
        self.assertEqual(response.status_code,200)
    def test_trackPlaylistReturnSuccess(self): 
        # The playlist API should return a 200 status with the id that has been added to the database   
        response = self.client.get(self.good_playlist_url, format='json')
        response.render() 
        self.assertEqual(response.status_code,200)
    def test_trackPlaylistReturn404(self): 
        # The playlist API should return a 404 status with the id that should not be in the database 
        response = self.client.get(self.bad_playlist_url, format='json')
        response.render() 
        self.assertEqual(response.status_code,404)
    # test API post status 
    def test_newPlaylistTrackReturnSuccess(self):
        url = reverse('playlist_tracks',kwargs={'playlist_id': '0'})  
        # add a new track 
        TrackFactory.create(pk='K4KK35KFL6L9L1NBJ20FDK')
        newtrack_data = {
            'track_id': 'K4KK35KFL6L9L1NBJ20FDK',
        }
        response = self.client.post(url, data=newtrack_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(PlaylistTrack.objects.count(), 1) #There should be only 1 record which was added in start up
    def test_newPlaylistTrackReturnSuccess(self):
        url = reverse('playlist_tracks',kwargs={'playlist_id': 'CD9002MLF9D9ISJ3I4KC5Y'})  
        # add a new track 
        TrackFactory.create(pk='K4KK35KFL6L9L1NBJ20FDK')
        newtrack_data = {
            'track_id': 'K4KK35KFL6L9L1NBJ20FDK',
        }
        response = self.client.post(url, data=newtrack_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(PlaylistTrack.objects.count(), 2) #There should be 2 records, one added in start up and one added in this test case


    # test API response columns 
    def test_trackArtistColumns(self): 
        response = self.client.get(self.good_artist_url, format='json')
        response.render() 
        data = json.loads(response.content)
        self.assertTrue('name' in data[0])
        self.assertTrue('artist' in data[0])
        self.assertTrue('release_date' in data[0])
        self.assertTrue('duration_ms' in data[0])
    def test_trackDanceColumns(self): 
        response = self.client.get(self.good_dance_url)
        response.render() 
        data = json.loads(response.content)
        self.assertTrue('name' in data[0])
        self.assertTrue('artist' in data[0])
        self.assertTrue('release_date' in data[0])
        self.assertTrue('duration_ms' in data[0])
    def test_trackWordyColumns(self): 
        response = self.client.get(self.good_wordy_url)
        response.render() 
        data = json.loads(response.content)
        self.assertTrue('name' in data[0])
        self.assertTrue('artist' in data[0])
        self.assertTrue('release_date' in data[0])
        self.assertTrue('duration_ms' in data[0])
    def test_trackPlaylistColumns(self): 
        response = self.client.get(self.good_playlist_url)
        response.render() 
        data = json.loads(response.content)
        self.assertTrue('name' in data[0])
        self.assertTrue('artist' in data[0])
        self.assertTrue('release_date' in data[0])
        self.assertTrue('duration_ms' in data[0])

    # test API response values 
    def test_trackAllArtistCorrect(self): 
        response1 = self.client.get(self.good_artist_url, format='json')
        response1.render() 
        data1 = json.loads(response1.content)
        self.assertTrue(data1[0]['name'],'Shamie')
        response2 = self.client.get(self.good_dance_url, format='json')
        response2.render() 
        data2 = json.loads(response2.content)
        self.assertTrue(data2[0]['name'],'Shamie')
        response3 = self.client.get(self.good_wordy_url, format='json')
        response3.render() 
        data3 = json.loads(response3.content)
        self.assertTrue(data3[0]['name'],'Shamie')
        response4 = self.client.get(self.good_playlist_url, format='json')
        response4.render() 
        data4 = json.loads(response4.content)
        self.assertTrue(data4[0]['name'],'Shamie')
    
    
# Create your tests here.
class SerializerTests(APITestCase): 
    track = None 
    trackSerializer = None 
    playlist = None 
    playlistSerializer = None 
    playlistTrack = None 
    playlistTrackSerializer = None 

    def setUp(self):
        self.track = TrackFactory.create(pk='JF03M5KFL6L9L1NBJ2JM4T', artist='Shamie')
        self.trackSerializer = TrackSerializer(instance=self.track)
        self.playlist = PlaylistFactory.create(pk='CD9002MLF9D9ISJ3I4KC5Y',name='Sample Playlist',genre='rock')
        self.playlistSerializer = PlaylistSerializer(instance=self.playlist)
        self.playlistTrack = PlaylistTrackFactory.create(track_id=self.track, playlist_id=self.playlist)
        self.playlistTrackSerializer = PlaylistTrackSerializer(instance=self.playlistTrack)

    def tearDown(self):
        # remove all the records that were added to the database after test is run 
        Track.objects.all().delete()
        Playlist.objects.all().delete()
        PlaylistTrack.objects.all().delete() 

    def test_trackSerializerStructure(self): 
        # check that the serializer structure is as expected
        data = self.trackSerializer.data 
        self.assertEqual(set(data.keys()), set(['track_id','name','artist','release_date','duration_ms']))  
    def test_trackSerializerRecords(self): 
        data = self.trackSerializer.data 
        self.assertEqual(data['track_id'],'JF03M5KFL6L9L1NBJ2JM4T')
        self.assertEqual(data['artist'],'Shamie')

    def test_playlistSerializerStructure(self): 
        # check that the serializer structure is as expected
        data = self.playlistSerializer.data 
        self.assertEqual(set(data.keys()), set(['name','genre']))  
    def test_playlistSerializerRecords(self): 
        data = self.playlistSerializer.data 
        self.assertEqual(data['name'],'Sample Playlist')
        self.assertEqual(data['genre'],'rock')

    def test_playlisttrackSerializerStructure(self): 
        # check that the serializer structure is as expected
        data = self.playlistTrackSerializer.data 
        self.assertEqual(set(data.keys()), set(['playlist_id', 'track_id']))  
    def test_playlisttrackSerializerRecords(self): 
        data = self.playlistTrackSerializer.data 
        self.assertEqual(data['track_id'],'JF03M5KFL6L9L1NBJ2JM4T')
        self.assertEqual(data['playlist_id'],'CD9002MLF9D9ISJ3I4KC5Y')