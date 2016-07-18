from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import UserData
from django.http import HttpResponseRedirect,HttpResponse
from custom.models import MyUser


def get_lang(request):
		try:
			current_language=UserData.objects.get(user_id=request.user.id).pref_language
		except UserData.DoesNotExist:
			current_language=request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru').split('-')[0]
		if request.user.is_authenticated():
				return HttpResponseRedirect('/%s/create_album'% current_language)
		else:
				return HttpResponseRedirect('/%s/login'% current_language)




def ajax(request):
		url="/".join(request.get_full_path().split('/'))[3:]
		if request.user.is_authenticated():
				lang=UserData.objects.get(user_id=request.user.id)
				lang.pref_language=request.POST.get('lang','')
				lang.save()
				return HttpResponseRedirect(request.POST.get('lang','en')+url) 
		else:
				return  HttpResponseRedirect(request.POST.get('lang','en')+url)
		
