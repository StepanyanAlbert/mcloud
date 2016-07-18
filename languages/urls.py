from django.conf.urls import url,include
from . import views 

urlpatterns=[
				url(r'[^/.]/ajax/$',views.ajax,name='ajax'),
				url(r'^$',views.get_lang,name='get-lang'),
			]
