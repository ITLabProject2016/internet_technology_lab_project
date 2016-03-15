from django.conf.urls import patterns, url
from zombies import views


# Patterns we are using on zombies project. If the user enters something that matches
# any of these URLs (after "zombies/"), appropriate view will be shown.
# Please comment liberally if you do something fancy with URLs.
urlpatterns = patterns(
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.profile, name='profile'),
    #url(r'^story-point/(?P<spid>\d+)/$', views.story_point, name='story-point'),
    url(r'^index-min/$', views.index_min, name='index-min'),
    url(r'^story-point/(?P<sid>\d+)/(?P<spid>\d+)/$', views.story_point, name='story-point'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^survivors/$', views.survivors, name='survivors'),
    url(r'^survivor/(?P<username>.*)/$', views.survivor_profile, name='survivor_profile'),
)
