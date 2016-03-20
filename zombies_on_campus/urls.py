from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from registration.backends.simple.views import RegistrationView


# Registration add-on: when user registers, redirect to home page
class MyRegistrationView(RegistrationView):
    def get_success_url(request, user):
        return '/zombies/'


urlpatterns = patterns('',
                       url(r'^$', include('zombies.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^zombies/', include('zombies.urls')),
                       url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT, }, name='media'),
                       )
