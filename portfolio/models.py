from django.db import models

class AboutMe(models.Model):
	full_name = models.CharField(default="Full Name", max_length=100, unique=False)
	title = models.CharField(default="Career Title", max_length=100, unique=False)
	phone = models.CharField(default="Phone Number", max_length=100, unique=False)
	email = models.CharField(default="email@email.com", max_length=100, unique=False)
	github_handle = models.CharField(default="mygithubhandle", max_length=100, unique=False)
	linkedin_url = models.CharField(default='https://linkedin.com/yourlinkedin', max_length=300, unique=False)
	location = models.CharField(default="495 Your address here", max_length=100, unique=False)
	content = models.TextField(blank=True)
	profile_pic = models.ImageField(default='default.png', upload_to='profile_pics', blank=True)
	resume = models.FileField(upload_to='resumes', blank=True)
	work_experience = models.BooleanField(default=True)

class Certification(models.Model):
	title = models.CharField(max_length=100, unique=False)
	description = models.TextField(blank=False)
	location = models.CharField(max_length=100, blank=False)
	link = models.CharField(max_length=200, blank=False)
	date_acheived = models.CharField(max_length=200, blank=False)
	image = models.ImageField(upload_to='certification_pics', blank=False)

	def __str__(self):
	   return str(self.title)

class Skill(models.Model):
	image = models.ImageField(default='default.png', upload_to='skills_pics', blank=True)
	title = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return str(self.title)

class WorkExperience(models.Model):
	title = models.CharField(max_length=100, unique=True, primary_key=True)
	link = models.CharField(max_length=200, blank=True)
	location = models.CharField(max_length=100, unique=False)
	start_date = models.CharField(max_length=200, blank=True)
	end_date = models.CharField(max_length=200, blank=True)
	total_time = models.CharField(max_length=200, blank=True)
	content = models.TextField(blank=False)

	def __str__(self):
		return str(self.title)

class WebsiteIcon(models.Model):
	image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True)