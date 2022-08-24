from django.shortcuts import render
from .models import Photo

def photography(request):
    
    photos = Photo.objects.all()[::-1]

    context = {
        'photos': photos
    }

    return render(request, 'photography/photos.html', context)

def photo(request, photo_id):

    photo = Photo.objects.get(id = photo_id)

    context = {
        'photo': photo
    }

    return render(request, 'photography/photo_post.html', context)