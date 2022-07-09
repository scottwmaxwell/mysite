from django.shortcuts import render

from projects.models import project
from blog.models import blogpost

# For Portfolio
from .models import AboutMe
from .models import Certifications
from .models import Skills
from .models import WorkExperience
from .models import ProfilePic
from .models import WebsiteIcon

def portfolio(request):

	# Get last 4 projects
	projectposts = project.objects.all()[::-1][:4]

	# Get last 4 blog posts
	blogposts = blogpost.objects.all()[::-1][:4]

	# Get AboutMe
	about_me = AboutMe.objects.all()[0]

	# Get Certifications
	certifications = Certifications.objects.all()

	# Get Skills
	skills = Skills.objects.all()

	# Get WorkExperience
	workexperience = WorkExperience.objects.all()

	# Get ProfilePic
	profilepic = ProfilePic.objects.all()[0]

	# Get website icon
	website_icon = WebsiteIcon.objects.all()[0]

	context = {
		'projectposts':   projectposts,
		'blogposts':      blogposts,
		'about_me':       about_me,
		'certifications': certifications,
		'skills':         skills,
		'workexperience': workexperience,
		'profilepic':     profilepic,
		'website_icon':	  website_icon,
	}
	
	return render(request, 'portfolio/portfolio.html', context)