from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'relaypi.views.home', name='home'),
    url(r'^relay/(?P<relay_id>\d+)/$', 'hardware.views.control', name='control'),

    url(r'^admin/', include(admin.site.urls)),
)
