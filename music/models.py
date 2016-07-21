from django.contrib.auth.models import Permission
from django.db import models
from custom.models import MyUser 

class Album(models.Model):
    user = models.ForeignKey(MyUser, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(width_field='image_width', height_field='image_height')
    image_width=models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    image_height=models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
