from django import forms
from .models import * 

class CountForm(forms.Form): 
    n = forms.IntegerField(label='Number of tracks')
    def clean(self): 
        cleaned_data = super(CountForm, self).clean()
        n = cleaned_data.get('n')
        if n <1 or n>50:
            raise forms.ValidationError("Please enter a number between 1-50.")
        return cleaned_data

class PlaylistForm(forms.Form): 
    name = forms.CharField(label = 'Playlist Name', max_length=256)
    genre = forms.CharField(label = 'Playlist Genre', max_length=50)

    def clean(self): 
        cleaned_data = super(PlaylistForm, self).clean()
        genre = cleaned_data.get('genre')

        if not genre in ('pop', 'rap', 'rock', 'latin', 'r&b','edm'):
            raise forms.ValidationError("Genre has to be a one of the following values: pop, rap, rock, latin, r&b, and edm")
        return cleaned_data
