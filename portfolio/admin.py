from django.contrib import admin

from django.db import models
from tinymce.widgets import TinyMCE

from .models import AboutMe, Certification, Skill, WorkExperience, ProfilePic, WebsiteIcon

class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }

class testAdmin(admin.ModelAdmin):
   list_display=["title"]

# Use TinyMCE Editor
admin.site.register(AboutMe, textEditorAdmin)
admin.site.register(WorkExperience, textEditorAdmin)

# Don't use TinyMCE Editor
admin.site.register(Certification)
admin.site.register(Skill)
admin.site.register(ProfilePic)
admin.site.register(WebsiteIcon)