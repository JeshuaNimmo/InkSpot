from django.db import models
from django.contrib.auth.models import User  # <-- THIS LINE is needed!

class TattooArtist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=600)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    website = models.URLField(blank=True)
    tattoo_picture1 = models.ImageField(upload_to='tattoo_pics/', blank=True, null=True)
    tattoo_picture2 = models.ImageField(upload_to='tattoo_pics/', blank=True, null=True)
    tattoo_picture3 = models.ImageField(upload_to='tattoo_pics/', blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    STYLE_CHOICES = [
        ('traditional', 'Traditional'),
        ('fineline', 'Fineline'),
        ('realism_color', 'Realism (Color)'),
        ('realism_blackgrey', 'Realism (Black & Grey)'),
        ('newschool', 'New School'),
        ('blackwork', 'Black Work'),
        ('coverup', 'Cover Up'),
        ('neotraditional', 'Neo-Traditional'),
    ]
    style = models.CharField(max_length=50, choices=STYLE_CHOICES, default='traditional')

    def __str__(self):
        return f"{self.user.username}'s Profile"