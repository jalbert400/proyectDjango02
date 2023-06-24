from __future__ import unicode_literals 
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from django.utils.encoding import python_2_unicode_compatible
from six import python_2_unicode_compatible


# Create your models here.
#Creo la clase Post y para que funcione como modelo deben heredar del models.Model 
@python_2_unicode_compatible 

class Post(models.Model):
	STATUS = (
		('draft','Draft'),
		('published','Published')
	)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique_for_date='publish')
	author = models.ForeignKey(User,related_name="blog_post", blank=True, null=True, on_delete=models.CASCADE)
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateField(auto_now=True)
	status = models.CharField(max_length=20,choices=STATUS,default='draft')

	#Esta clase se usara para ordenar los resultados de publish en el tiempo que se publico en este caso con - es descendete
	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title
