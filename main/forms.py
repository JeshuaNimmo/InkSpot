from django import forms
from .models import TattooArtist

class TattooArtistForm(forms.ModelForm):
    class Meta:
        model = TattooArtist
        fields = [
            'profile_picture',
            'bio',
            'instagram',
            'facebook',
            'website',
            'tattoo_picture1',
            'tattoo_picture2',
            'tattoo_picture3',
            'city',
            'state',
            'style',   
        ]