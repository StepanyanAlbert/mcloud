from django.contrib.auth.decorators import login_required
from django.conf.urls import url,include
from . import views

app_name = 'custom'

urlpatterns=[
				url(r'^home/$',views.Home.as_view(),name='home'),
				url(r'^login/$',views.redir,name='login'),
				url(r'^welcome/$',views.check,name='check-login'),
				url(r'^homepage/$',views.welcome,name='homepage'),
				url(r'^logout/$',views.logout,name='logout'),
				url(r'^update/(?P<pk>\d+)/$',login_required(views.UpdateUser.as_view()),name='update'),
				]
