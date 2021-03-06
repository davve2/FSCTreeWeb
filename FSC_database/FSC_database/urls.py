"""FSC_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView

from FrancisellaDatabase.views import (
	user_listview,
	UserListView,
	UserDetailView,
	UserCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(),name="login"),
    path('users/', UserListView.as_view()),
    path('users/create', UserCreateView.as_view()),
    path('users/<str:slug>/', UserDetailView.as_view()),
    path('', TemplateView.as_view(template_name="home.html")),
    path('info/', TemplateView.as_view(template_name="info.html")),
    path('contact/', TemplateView.as_view(template_name="contact.html")),
]
