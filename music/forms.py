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
			if not file.name.split('.')[-1] in self.IMAGE_FILE_TYPES:
				raise forms.ValidationError('Image file must have jpg , png or jpeg extension')
			if file._size>1024*1024:
					raise forms.ValidationError('Image ile too large')
			return file	


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']
	#def clean_audio_file(self):
	#		audio=self.cleaned_data['']

