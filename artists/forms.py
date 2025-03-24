# artists/forms.py
from django import forms
from .models import TattooArtist

class TattooArtistForm(forms.ModelForm):
    class Meta:
        model = TattooArtist
        fields = ['name', 'bio', 'location', 'instagram']  # remove 'styles' and 'profile_image'