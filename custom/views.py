from django.conf import settings
from django.utils.translation import get_language
from django.contrib.auth import authenticate, login                                                           
from django.contrib.auth import logout as django_logout                                             
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView,View,UpdateView
from .admin import UserCreationForm,UserChangeForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import MyUser
from languages.models import UserData
from django.contrib.auth.views import password_reset
from languages.views import get_lang



class Home(CreateView):
		form_class=UserCreationForm
		template_name='custom/register.html'
		success_url=reverse_lazy('custom:login')




def redir(request):
		return render(request,'custom/login.html')




def check(request):
			if request.method=='POST':
				email=request.POST['email']
				password=request.POST['password']
				remember_me=request.POST.get('remember','')
				if not remember_me:
						settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
				else:
						settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
				user = authenticate(username=email, password=password)
				if user is not None:
						if user.is_active:
								login(request,user)
								return HttpResponseRedirect('/%s/homepage/' % get_language()  )
			return render(request, 'custom/login.html', {'error_message': 'Invalid login'}) 


def  welcome(request):
		template_name='music/info.html'
		return render(request,template_name)



def logout(request):
		django_logout(request)
		return HttpResponseRedirect('/%s/login' % get_language())



class UpdateUser(UpdateView):
		model=MyUser
		form_class=UserChangeForm
		template_name= 'custom/update_form.html'
		def get_success_url(self):
				return reverse_lazy('custom:homepage')
		def get_object(self, queryset=None):
				return self.request.user




