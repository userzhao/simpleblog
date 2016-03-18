from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	repassword=models.CharField(max_length=20)
	email = models.EmailField()

	def __unicode__(self):
		return self.username	

class Post(models.Model):
	title=models.CharField(max_length=20)
	desc = models.CharField(max_length=40)
	content=models.TextField()
	created_time = models.DateTimeField(default=timezone.now())
	published_time = models.DateTimeField(default=None,null=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def publish(self):
		self.published_time = timezone.now()
		self.save()

	class Meta:
		ordering=['-created_time']

class Comment(models.Model):
	post = models.ForeignKey(Post)
	content = models.TextField()
	comment_time=models.DateTimeField(timezone.now())
	class Meta:
		ordering = ['-comment_time']
		
