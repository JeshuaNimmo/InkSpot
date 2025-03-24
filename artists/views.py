from django.shortcuts import render, redirect
from .models import TattooArtist
from .forms import TattooArtistForm

def artist_list(request):
    location_query = request.GET.get('location', '')
    style_query = request.GET.get('style', '')
    
    artists = TattooArtist.objects.all()
    if location_query:
        artists = artists.filter(location__icontains=location_query)
    if style_query:
        artists = artists.filter(styles__name__icontains=style_query)
    artists = artists.distinct()
    
    return render(request, 'artist_list.html', {'artists': artists})

def add_artist(request):
    if request.method == 'POST':
        form = TattooArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = TattooArtistForm()
    return render(request, 'add_artist.html', {'form': form})