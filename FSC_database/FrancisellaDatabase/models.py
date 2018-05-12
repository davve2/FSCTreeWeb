from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=200,null=True,blank=False)
	email = models.EmailField(max_length=254,null=True,blank=False)
	location = models.CharField(max_length=200,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)