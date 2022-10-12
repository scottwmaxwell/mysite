from django.db import models
from django.utils import timezone

class project(models.Model):
	title = models.CharField(max_length=100, unique=True)
	description = models.CharField(max_length=200, blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	content = models.TextField(blank=True)
	website_link = models.CharField(max_length=100, unique=False, default='', blank=True)
	code_link = models.CharField(max_length=100, unique=False, default='', blank=True)
	image = models.ImageField(upload_to='project_pics', blank=True)

	def __str__(self):
		return str(self.title)


# Where the main extension resides
class chrome_extension(models.Model):
	title = models.CharField(max_length=100, unique=True)
	file = models.FileField(upload_to='application', blank=True)

	def __str__(self):
		return str(self.title)

# Where the XML file
class chrome_extension_update(models.Model):
	title = models.CharField(max_length=100, unique=True)
	xml_file = models.FileField(upload_to='chrome_extension_updates', blank=True)

	def __str__(self):
		return str(self.title)
