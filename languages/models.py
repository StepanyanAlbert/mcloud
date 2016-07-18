from django.db import models
from custom.models import MyUser

class UserData(models.Model):
		l_choices=(('en','English'),('hy','Armenain'),('ru','Russian'))
		user=models.OneToOneField(MyUser)
		pref_language=models.CharField(max_length=3,default='hy',choices=l_choices)
