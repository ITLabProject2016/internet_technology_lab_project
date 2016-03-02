from django.conf.urls import patterns, url
from zombies import views


# Patterns we are using on zombies project. If the user enters something that matches
# any of these URLs (after "zombies/"), appropriate view will be shown.
# Please comment liberally if you do something fancy with URLs.
urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^story/$', views.story, name='story'),
    url(r'^the-end/$', views.the_end, name='the_end'),
    url(r'^story-change/$', views.story_change, name='story-change'),
)

