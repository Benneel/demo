from django.db import models

class client(models.Model):
	number		= models.CharField(max_length=200)
	lastname	= models.CharField(max_length=200)
	status		= models.BooleanField(default=True)
	def __unicode__(self):
		FullName = "%s %s" %(self.number, self.lastname)
		return FullName

class production(models.Model):
	number		= models.CharField(max_length=200)
	description	= models.TextField(max_length=300)
	status		= models.BooleanField(default=True)
	def __unicode__(self):
		return self.number
