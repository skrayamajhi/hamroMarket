from django.shortcuts import render
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_protect 

from login.login_form import LoginForm 

# Create your views here.
from django.http import HttpResponse 

@csrf_protect
def login(request):
	if request.method == 'POST':
		login = LoginForm(request.POST)
		if login.is_valid():
			return HttpResponse("Logged in")
		else:
			return HttpResponse("Error while loggin in.")
	else:
		csrfContext = RequestContext(request)
		login_form = LoginForm()
		return render(request,'login.html',{'form': login_form},csrfContext)

