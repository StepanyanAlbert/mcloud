from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import AlbumForm, SongForm
from .models import Album, Song
from django.views.generic.edit  import CreateView
from django.views.generic  import ListView,DetailView 
from django.core.urlresolvers import reverse_lazy



AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg','mpeg']

class  CreateAlbum(CreateView):
		form_class=AlbumForm
		template_name='music/create_album.html'
		success_url=reverse_lazy('music:index')

class AlbumDetailView(DetailView):
    model = Album

class CreateSong(CreateView):
		form_class=SongForm
		template_name='music/create_song.html'
		

@login_required
def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.song_set.all()
        for s in albums_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'album': album,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'music/create_song.html', context)

        song.save()
        return render(request, 'music/album_detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)

@login_required
def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'albums': albums})

@login_required
def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/album_detail.html', {'album': album})


@login_required
def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

@login_required
def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

class Homepage(ListView):
		model=Album
		template_name='music/index.html'
		context_object_name='albums' 
		def get_queryset(self):
				return Album.objects.filter(user_id=self.request.user.id)
       #albums = Album.objects.filter(user=request.user)
       # song_results = Song.objects.all()
       # query = request.GET.get("q")
       # if query:
       #     albums = albums.filter(
       #         Q(album_title__icontains=query) |
       #         Q(artist__icontains=query)
       #     ).distinct()
       #     song_results = song_results.filter(
       #         Q(song_title__icontains=query)
       #     ).distinct()
       #     return render(request, 'music/index.html', {
       #         'albums': albums,
       #         'songs': song_results,
       #     })
       # else:
       # return render(request, 'music/index.html', {'albums': albums})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)

@login_required
def songs(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        try:
            song_ids = []
            for album in Album.objects.filter(user=request.user):
                for song in album.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Album.DoesNotExist:
            users_songs = []
        return render(request, 'music/songs.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })

def song_create_existing_album(request):
		get_all_albums=Album.objects.filter(user=request.user)
		return render(request,'music/selectbox_albums.html',{'albums':get_all_albums})
		
def checker(request,fieldname,template_name,kwargs):
		field=request.POST.get(fieldname,'')
		if not field:
				return render(request,template_name,**kwargs)

def cs_album_id(request):
		get_albums=Album.objects.filter(user=request.user)
		if request.method=='POST':
				song_title=request.POST.get('song_title','')
				song=request.FILES.get('song_file')
				album_id=request.POST.get('album_id','')
				checker(request,'song_title','music/selectbox_albums.html',{'valid_error_title':' * This field is required','albums':get_albums})
				checker(request,'album_id','music/selectbox_albums.html',{'valid_error_title':' * This field is required','albums':get_albums})
				if not song:
						return render(request,'music/selectbox_albums.html',{'valid_error_audio':' * This field is required','albums':get_albums})
				if not ''.join(song.content_type.split('/')[1:])  in AUDIO_FILE_TYPES:
						return render(request,'music/selectbox_albums.html',{'valid_error_audio':'%s Audio files must have mp3,wav,or ogg extension' % ''.join(song.content_type.split('/')[1:]),'albums':get_albums})
				else:
						return HttpResponse( ''.join(song.content_type.split('/')[1:]))
		return render(request,'music/selectbox_albums.html',{'error_message':'Something wnet wrong','albums':get_albums})


