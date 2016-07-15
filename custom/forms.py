from django import forms

class PasswordResetRequestForm(forms.Form):
	    email_or_username = forms.CharField(label=("Email"), max_length=254)
