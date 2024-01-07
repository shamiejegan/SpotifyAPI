from django.contrib import admin

from .models import * 

# Register your models here.
class PlaylistTrackInLine(admin.TabularInline):
    model = PlaylistTrack
    extra = 3

class TrackAdmin(admin.ModelAdmin):
    list_display = ('track_id','name','artist','popularity','release_date','danceability','wordiness','duration_ms')
admin.site.register(Track, TrackAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('playlist_id','name','genre')
    inlines = [PlaylistTrackInLine]
admin.site.register(Playlist, PlaylistAdmin)

