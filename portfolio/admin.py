from django.contrib import admin

from django.db import models
from tinymce.widgets import TinyMCE

from .models import AboutMe, Certifications, Skills, WorkExperience, ProfilePic, WebsiteIcon

class textEditorAdmin(admin.ModelAdmin):
   list_display = ["content"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }

# Use TinyMCE Editor
admin.site.register(AboutMe, textEditorAdmin)
admin.site.register(WorkExperience, textEditorAdmin)

# Don't use TinyMCE Editor
admin.site.register(Certifications)
admin.site.register(Skills)
admin.site.register(ProfilePic)
admin.site.register(WebsiteIcon)