from django.db import models
import uuid

# Create your models here.
class Track(models.Model):
    track_id = models.CharField(max_length=256, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=256, null=False, blank=False)
    artist = models.CharField(max_length=256, null=False, blank=False)
    popularity = models.IntegerField(null=False, blank=True)
    release_date = models.DateField(null=False, blank=True)
    danceability = models.FloatField(null=False, blank=True)
    wordiness = models.FloatField(null=False, blank=True)
    duration_ms = models.IntegerField(null=False, blank=True)
    def __str__(self):
        return self.name

class Playlist(models.Model):
    playlist_id = models.CharField(max_length=256, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=256, null=False, blank=False)
    genre = models.CharField(max_length=50, null=False, blank=False)
    track = models.ManyToManyField(Track, through='PlaylistTrack')
    def __str__(self):
        return self.name
    # override default save method to add a new playlist id using the uuid package
    def save(self, *args, **kwargs):
        if not self.playlist_id:
            self.playlist_id = str(uuid.uuid4().hex[:22].upper())
        super().save(*args, **kwargs)


class PlaylistTrack(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete=models.DO_NOTHING)
    track_id = models.ForeignKey(Track, on_delete=models.DO_NOTHING)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['playlist_id', 'track_id'], name='playlist_track_id')
        ]
