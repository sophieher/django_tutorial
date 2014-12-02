## Food Mood URLs
from django.conf.urls import patterns, url
from food_mood import views

urlpatterns = patterns ('', 

    # web routes
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^entries/$', views.EntryView.as_view(), name='entries'),
    # ex: /entries/#{id}
    url(r'^entries/(?P<entry_id>\d+)/$', views.entry, name='entry'),
    url(r'add/$', views.add_food_mood, name='add'),
)