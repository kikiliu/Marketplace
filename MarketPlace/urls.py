from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'MarketPlace.views.home', name='home'),
    #url(r'^MarketPlace/', include('MarketPlace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^eventlist$', views.eventlist),
    url(r'^main/', views.main),

    url(r'^eventlist/', views.eventlist)

)
