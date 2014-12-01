## Project URLs
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')), which includes all views from blog

    url(r'^food_mood/', include('food_mood.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
