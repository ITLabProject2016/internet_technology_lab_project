from django.conf.urls import patterns, include, url
from django.contrib import admin
# Allows to access variables within settings.py file.
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zombies_on_campus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # This is where we connect different applications if we desire to make more than 1.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^zombies/', include('zombies.urls')),
)

# ONLY FOR DEVELOPMENT PURPOSES. SHOULD NOT BE DEPLOYED WITH THIS.
# If DEBUG is set to True, additional URL matching pattern appended to the existing one.
# For any requested file with with URL starting with media/, request will be sent to
# django.views.static view. Why here: allows users to upload media.
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )


