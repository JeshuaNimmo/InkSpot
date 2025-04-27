from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import TattooArtistForm
from .models import TattooArtist

# Home Page View
def home_view(request):
    return render(request, 'home.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

# Create Tattoo Artist Profile View
@login_required
def create_profile_view(request):
    # Check if user already has a profile
    if hasattr(request.user, 'tattooartist'):
        return redirect('artist_profile', artist_id=request.user.tattooartist.id)

    if request.method == 'POST':
        form = TattooArtistForm(request.POST, request.FILES)
        if form.is_valid():
            tattoo_artist = form.save(commit=False)
            tattoo_artist.user = request.user
            tattoo_artist.save()
            return redirect('artist_profile', artist_id=tattoo_artist.id)
    else:
        form = TattooArtistForm()

    return render(request, 'create_profile.html', {'form': form})

# Edit Tattoo Artist Profile View
@login_required
def edit_profile_view(request):
    tattoo_artist = request.user.tattooartist

    if request.method == 'POST':
        form = TattooArtistForm(request.POST, request.FILES, instance=tattoo_artist)
        if form.is_valid():
            form.save()
            return redirect('artist_profile', artist_id=tattoo_artist.id)
    else:
        form = TattooArtistForm(instance=tattoo_artist)

    return render(request, 'edit_profile.html', {'form': form})

# List All Tattoo Artists View
def artist_list_view(request):
    artists = TattooArtist.objects.all()

    city = request.GET.get('city')
    style = request.GET.get('style')

    if city:
        artists = artists.filter(city__icontains=city)
    if style:
        artists = artists.filter(style=style)

    return render(request, 'artist_list.html', {'artists': artists})

# Individual Tattoo Artist Profile View
def profile_view(request, artist_id):
    artist = TattooArtist.objects.get(id=artist_id)
    return render(request, 'profile.html', {'artist': artist})