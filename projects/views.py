from django.shortcuts import render

from .models import project
from portfolio.models import WebsiteIcon

def projects(request):

	posts = project.objects.all()[::-1]

	website_icon = WebsiteIcon.objects.all()[0]

	context = {
		'posts': posts,
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

