from .models import UserData


def current_lang(request):
		try:
			current_language=UserData.objects.get(user_id=request.user.id).pref_language
		except UserData.DoesNotExist:
			current_language=request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru').split('-')[0]
		return  current_language
