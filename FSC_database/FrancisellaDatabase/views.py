from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

import os
# Create your views here.

from .models import User
from .forms import UserCreateForm

def user_listview(request):
	template_name = 'users/user_list.html'
	queryset = User.objects.all()
	context = {
		"user_list": queryset
	}
	
	return render(request,template_name,context)

class UserListView(ListView):
	template_name = 'users/user_list.html'
	
	def get_queryset(self):
		location = self.kwargs.get("location")
		queryset = User.objects.all()
		if location:
			queryset = User.objects.filter(location__icontains=location)
		return queryset

class UserDetailView(DetailView):
	template_name = 'users/user_detail.html'
	queryset = User.objects.all()


#@login_required(login_url="/login/")
class UserCreateView(LoginRequiredMixin, CreateView):
	form_class = UserCreateForm
	template_name = "users/form.html"
	success_url= "/users/"

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.owner = self.request.user
		return super(UserCreateView, self).form_valid(form)