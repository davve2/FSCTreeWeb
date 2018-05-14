from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models.deletion import CASCADE

from .utils import unique_slug_generator
#from .validators import validate_location

User = settings.AUTH_USER_MODEL

# Create your models here.
class User(models.Model):
	owner = models.ForeignKey(User,on_delete=CASCADE)
	name = models.CharField(max_length=200,null=True,blank=False)
	email = models.EmailField(max_length=254,null=True,blank=False)
	location = models.CharField(max_length=200,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(null=True,blank=True,unique=True)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name


def snp_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(snp_pre_save_reciever,sender=User)


class CanSNP(models.Model):
	cansnp = models.CharField(max_length=20,null=True,blank=False)
	sname = models.CharField(max_length=100,null=True,blank=False)
	lname = models.CharField(max_length=100,null=True,blank=False)
	email = models.EmailField(max_length=254,null=True,blank=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(unique=True)
