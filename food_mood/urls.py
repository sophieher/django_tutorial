## Food Mood URLs
from django.conf.urls import patterns, url
from food_mood import views

urlpatterns = patterns ('', 

    # web routes
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^entries/$', views.entries, name='entries'),
    # ex: /entries/5/
    url(r'^entries/(?P<entry_id>\d+)/$', views.entry, name='entry'),
)