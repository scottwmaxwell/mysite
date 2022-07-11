from django.db import models

class AboutMe(models.Model):
	content = models.TextField(blank=True)

class Certifications(models.Model):
	title = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	location = models.CharField(max_length=100, blank=True)
	link = models.CharField(max_length=200, blank=True)
	date_acheived = models.CharField(max_length=200, blank=True)

	def __str__(self):
	   return str(self.title)

class Skills(models.Model):
	title = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return str(self.title)

class WorkExperience(models.Model):
	title = models.CharField(max_length=100, unique=False)
	link = models.CharField(max_length=200, blank=True)
	location = models.CharField(max_length=100, unique=False)
	start_date = models.CharField(max_length=200, blank=True)
	end_date = models.CharField(max_length=200, blank=True)
	total_time = models.CharField(max_length=200, blank=True)
	content = models.TextField(blank=False, primary_key=True)

	def __str__(self):
		return str(self.title)

class ProfilePic(models.Model):
	image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True)

class WebsiteIcon(models.Model):
	image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True)