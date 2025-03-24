from django.db import models

class TattooStyle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TattooArtist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    instagram = models.URLField(blank=True)
    styles = models.ManyToManyField(TattooStyle, blank=True)  # For tattoo styles
    profile_image = models.ImageField(upload_to='artist_profiles/', blank=True, null=True)

    def __str__(self):
        return self.name