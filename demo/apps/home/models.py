from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
		def url(self, filename):
			root = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
			return root

		user = models.OneToOneField(User)
		photo = models.ImageField(upload_to=url)
		telephone = models.CharField(max_length=30)

		def __unicode__(self):
			return self.user.username