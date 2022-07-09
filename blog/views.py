from django.shortcuts import render
from .models import blogpost
from portfolio.models import WebsiteIcon

def blog(request):

	website_icon = WebsiteIcon.objects.all()[0]
	posts = blogpost.objects.all()[::-1]
	context ={
		'posts': posts,
		'website_icon': website_icon
	}

	return render(request, 'blog/blog.html', context)


def blog_post(request, blog_id):

	website_icon = WebsiteIcon.objects.all()[0]
	text = blogpost.objects.get(id=blog_id)
	context = {
		'text':text,
		'website_icon': website_icon
	}

	return render(request, "blog/blog_post.html", context)