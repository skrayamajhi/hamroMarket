from django.db import models

# Create your models here.

class login(models.Model):
	first_name = models.CharField(max_length=20)
	password = models.CharField(max_length=30)
	