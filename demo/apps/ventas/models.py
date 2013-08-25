from django.db import models

class client(models.Model):
	number		= models.CharField(max_length=200)
	lastname	= models.CharField(max_length=200)
	status		= models.BooleanField(default=True)

	def __unicode__(self):
		FullName = "%s %s" %(self.number, self.lastname)
		return FullName

class production(models.Model):

	def url(self, filename):
		root = "MultimediaData/production/%s/%s"%(self.number,str(filename))
		return root

	number		= models.CharField(max_length=200)
	description	= models.TextField(max_length=300)
	status		= models.BooleanField(default=True)
	image		= models.ImageField(upload_to=url,null=True,blank=True)
	price		= models.DecimalField(max_digits=6,decimal_places=2)
	stock		= models.IntegerField()

	def __unicode__(self):
		return self.number
