from django.db import models
from django.utils import timezone
from portfolio.models import WebsiteIcon
from .models import Photo

class Post():
    title = models.CharField(max_length=100, unique=True)
    post_type = models.CharField(max_length=100, unique=True, blank=False)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=False, upload_to='photography_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=200, blank=True)
