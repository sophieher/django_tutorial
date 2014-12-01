## Food Mood URLs
from django.conf.urls import patterns, url
from food_mood import views

urlpatterns = patterns ('', 
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
)