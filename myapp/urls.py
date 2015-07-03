# Project URLs
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'myapp.views.index', name='index'),
    url(r'^food_mood/', include('food_mood.urls', namespace="food_mood")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    (r'^accounts/', include('allauth.urls')),
)
