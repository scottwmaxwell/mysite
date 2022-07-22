from django.shortcuts import render

from projects.models import project
from blog.models import blogpost

# For Portfolio
from .models import AboutMe
from .models import Certification
from .models import Skill
from .models import WorkExperience
from .models import WebsiteIcon

def portfolio(request):

	# Get last 4 projects
	projectposts = project.objects.all()[::-1][:4]

	# Get last 4 blog posts
	blogposts = blogpost.objects.all()[::-1][:4]

	# Get AboutMe
	about_me = AboutMe.objects.all()[0]

	# Get Certifications
	certifications = Certification.objects.all()

	# Get Skills
	skills = Skill.objects.all()

	# Get WorkExperience
	workexperience = WorkExperience.objects.all()[::-1]

	# Get website icon
	website_icon = WebsiteIcon.objects.all()[0]

	context = {
		'projectposts':   projectposts,
		'blogposts':      blogposts,
		'about_me':       about_me,
		'certifications': certifications,
		'skills':         skills,
		'workexperience': workexperience,
		'website_icon':	  website_icon,
	}
	
	return render(request, 'portfolio/portfolio.html', context)