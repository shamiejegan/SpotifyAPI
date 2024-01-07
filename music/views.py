from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import * 
from .forms import * 

# Create your views here.
def index(request): 
    return render(request, './music/index.html')

def artists(request): 
    artists = Track.objects.values_list('artist', flat=True).distinct()
    return render(request, './music/artists.html', {'artists': artists})

def dance(request): 
    form = CountForm()
    if request.method=='POST': 
        form = CountForm(request.POST)
        if form.is_valid(): 
            n = form.cleaned_data['n']
            return HttpResponseRedirect('api/tracks/dance/'+str(n))
        else: 
            return render(request, './music/dance.html', {'form':form,'error':'failed'})

    else: 
        return render(request, './music/dance.html',{'form':form})

def wordy(request): 
    form = CountForm()
    if request.method=='POST': 
        form = CountForm(request.POST)
        if form.is_valid(): 
            n = form.cleaned_data['n']
            return HttpResponseRedirect('api/tracks/wordy/'+str(n))
        else: 
            return render(request, './music/wordy.html', {'form':form,'error':'failed'})

    else: 
        return render(request, './music/wordy.html',{'form':form})


def playlists(request): 
    playlists = Playlist.objects.all()
    return render(request, './music/playlists.html',{'playlists': playlists})

def create_playlist(request): 
    if request.method=='POST': 
        form = PlaylistForm(request.POST)
        playlists = Playlist.objects.all()
        if form.is_valid(): 
            playlist = Playlist()
            playlist.name = form.cleaned_data['name']
            playlist.genre = form.cleaned_data['genre']
            playlist.save() #playlist id will be automatically generated 
            return HttpResponseRedirect('/create_playlist/')
        else: 
            return render(request,'./music/create_playlist.html', {'form':form,'error':'failed', 'playlists': playlists})
    else: 
        playlists = Playlist.objects.all()
        form = PlaylistForm()
        return render(request, './music/create_playlist.html', {'form':form, 'playlists': playlists})
    