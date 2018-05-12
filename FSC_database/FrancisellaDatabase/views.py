from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import os
# Create your views here.

from .models import User

def user_listview(request):
	print(os.getcwd())
	template_name = 'users/user_list.html'
	queryset = User.objects.all()
	context = {
		"user_list": queryset
	}
	
	return render(request,template_name,context)