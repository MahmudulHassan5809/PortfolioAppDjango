from django.db import models


from datetime import datetime

# Create your models here.


class Job(models.Model):
	image = models.ImageField(upload_to='photos/%Y/%m/%d/')
	summary = models.CharField(max_length=200)


	# def __str__(self):
	# 	return self.name
