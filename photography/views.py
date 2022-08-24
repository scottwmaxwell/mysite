from django.shortcuts import render
from .models import Photo
from portfolio.models import WebsiteIcon

def photography(request):
    
    photos = Photo.objects.all()[::-1]
    website_icon = WebsiteIcon.objects.all()[0]

    context = {
        'photos': photos,
        'website_icon': website_icon
    }

    return render(request, 'photography/photos.html', context)

def photo(request, photo_id):

    photo = Photo.objects.get(id = photo_id)
    website_icon = WebsiteIcon.objects.all()[0]

    context = {
        'photo': photo,
        'website_icon': website_icon
    }

    return render(request, 'photography/photo_post.html', context)