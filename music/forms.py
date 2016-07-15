from django import forms
from django.contrib.auth.models import User
from .models import Album, Song

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']


class AlbumForm(forms.ModelForm):

	IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
	class Meta:
			model = Album
			fields = ['artist', 'album_title', 'genre', 'album_logo']
	def clean_album_logo(self):
			file=self.cleaned_data.get('album_logo')
			#filetype = magic.from_buffer(file.read())
			if not file.name.split('.')[-1] in self.IMAGE_FILE_TYPES:
				raise forms.ValidationError('Image file must have jpg , png or jpeg extension')
			return file	


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


