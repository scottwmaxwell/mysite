from django.db import models
from django.utils import timezone

class Photo(models.Model):
    caption = models.TextField(blank=True)
    image = models.ImageField(blank=False, upload_to='photography_pics')
    date_posted = models.DateTimeField(default=timezone.now)