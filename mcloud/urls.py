from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = i18n_patterns(
				url(r'^admin/', admin.site.urls),  
				url(r'^', include('custom.urls')), 
				url(r'^', include('languages.urls')), 
				url(r'^', include('music.urls')), 
				url(r'^', include('password_reset.urls')), 
				)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
				               static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
