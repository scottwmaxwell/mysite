from django.db import models
from django.utils import timezone

class blogpost(models.Model):
   title = models.CharField(max_length=100, unique=True)
   content = models.TextField(blank=True)
   date_posted = models.DateTimeField(default=timezone.now)
   link = models.CharField(max_length=200, blank=True)

   def __str__(self):
       return str(self.title)