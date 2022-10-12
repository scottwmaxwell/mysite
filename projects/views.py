from django.shortcuts import render

from .models import project
from .models import chrome_extension
from portfolio.models import WebsiteIcon

def projects(request):

	project_posts = project.objects.all()[::-1]

	website_icon = WebsiteIcon.objects.all()[0]

	context = {
		'projects': project_posts,
		'website_icon': website_icon
	}
	
	return render(request, 'projects/projects.html', context)

def project_post(request, project_id):

	website_icon = WebsiteIcon.objects.all()[0]
	projectpost = project.objects.get(id=project_id)

	context = {
		'project': projectpost,
		'website_icon': website_icon
	}

	return render(request, 'projects/project_post.html', context)

def chrome_extensions(request):

	website_icon = WebsiteIcon.objects.all()[0]
	chrome_extensions = chrome_extension.objects.all()

	context = {
		'website_icon': website_icon,
		'extensions': chrome_extensions
	}

	return render(request, 'projects/chrome_extensions.html', context)


