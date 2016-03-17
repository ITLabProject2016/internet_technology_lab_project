from django.conf.urls import patterns, include, url
from django.contrib import admin
# Allows to access variables within settings.py file.
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from django.conf.urls.static import static


# Registration add-on: when user registers, redirect to home page
class MyRegistrationView(RegistrationView):
    # In TwD12, uses self. Lots of errors with it, so I removed it
    # Not too sure of the consequences, but seems to work. -Simonas
    def get_success_url(request, user):
        return '/zombies/profile_pic/'


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^zombies/', include('zombies.urls')),
                       url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}, name='media'),
                       )
              #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ONLY FOR DEVELOPMENT PURPOSES. SHOULD NOT BE DEPLOYED WITH THIS.
# If DEBUG is set to True, additional URL matching pattern appended to the existing one.
# For any requested file with with URL starting with media/, request will be sent to
# django.views.static view. Why here: allows users to upload media.