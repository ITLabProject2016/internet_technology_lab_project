from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zombies_on_campus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # This is where we connect different applications if we desire to make more than 1.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^zombies/', include('zombies.urls')),
)


