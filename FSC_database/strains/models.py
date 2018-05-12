from django.db import models

# Create your models here.
class Strains(models.Model):
	name = models.CharField(max_length=200)
	SNP = models.CharField(max_length=10)
