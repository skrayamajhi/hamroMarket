from django import forms 
from login.models import login

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = login 
		fields = "__all__"
		labels = {
			'username': 'Username',
			'password': 'Password'
		}

#selecting some fields 
# fields = ('first_name', 'last_name',)
