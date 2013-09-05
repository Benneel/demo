from django.db import models

class client(models.Model):
	number		= models.CharField(max_length=200)
	lastname	= models.CharField(max_length=200)
	status		= models.BooleanField(default=True)

	def __unicode__(self):
		FullName = "%s %s" %(self.number, self.lastname)
		return FullName

class productCategory(models.Model):
	number = models.CharField(max_length=200)
	description = models.TextField(max_length=400)

	def __unicode__(self):
		return self.number

class production(models.Model):

	def url(self, filename):
		root = "MultimediaData/production/%s/%s"%(self.number,str(filename))
		return root

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px height=50px/></a>'%(self.image, self.image)

	thumbnail.allow_tags = True

	number		= models.CharField(max_length=200)
	description	= models.TextField(max_length=300)
	status		= models.BooleanField(default=True)
	image		= models.ImageField(upload_to=url,null=True,blank=True)
	price		= models.DecimalField(max_digits=6,decimal_places=2)
	stock		= models.IntegerField()
	category 	= models.ManyToManyField(productCategory, null=True, blank=True)

	def __unicode__(self):
		return self.number
