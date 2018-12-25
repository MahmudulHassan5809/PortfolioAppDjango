from django.db import models


from datetime import datetime

# Create your models here.


class Blog(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='blog/%Y/%m/%d/')
	body = models.TextField()
	pub_date = models.DateTimeField()


	def __str__(self):
		return self.title


	def summary(self):
		return self.body[:80] + '....'

