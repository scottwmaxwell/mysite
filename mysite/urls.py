from django.contrib import admin
from django.urls import path, include

# model views
from portfolio import views as portfolio_views
from blog import views as blog_views
from projects import views as projects_views
from photography import views as photography_views
from django.conf import settings
from django.conf.urls.static import static

# authentication view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_views.portfolio, name='portfolio'),
    path('projects/', projects_views.projects, name='projects'),
    path('projects/projectpost/<project_id>', projects_views.project_post, name='project_post'),
    path('blog/', blog_views.blog, name = 'blog'),
    path('blog/blogpost/<blog_id>', blog_views.blog_post, name = 'blog_post'),
    path('photography/', photography_views.photography, name= 'photography'),
    path('projects/chrome_extensions', projects_views.chrome_extensions, name= 'chrome_extensions'),
    path('photography/photo/<photo_id>', photography_views.photo, name='photo'),
    path('tinymce/',include('tinymce.urls')),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)