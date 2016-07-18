from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^music/$', login_required(views.Homepage.as_view()), name='index'),
    #url(r'^register/$', views.register, name='register'),
	#url(r'^',include('custom.urls')),
    #url(r'^login_user/$', views.login_user, name='login_user'),
    #url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^create_album/$', login_required(views.CreateAlbum.as_view()), name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]
