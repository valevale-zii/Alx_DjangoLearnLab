from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers_set', blank=True
    )
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='following_set', blank=True
    )

    def __str__(self):
        return self.username
