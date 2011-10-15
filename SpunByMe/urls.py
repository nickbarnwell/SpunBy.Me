from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #API Lines
    ('^search/', 'common.views.search'),
    ('^party/(?P<pid>\d+)/add_song', 'common.views.add_song'),
    ('^party/(?P<pid>\d+)/queue', 'common.views.queue'),
    ('^party/(?P<pid>\d+)/next', 'common.views.get_next_song'),
    ('^party/(?P<pid>\d+)/playing', 'common.views.now_playing'),

    #View Lines
    ('^login/', 'desktop.views.login'),
    ('^party/new', 'desktop.views.new_party'),
    ('^party/(?P<slug>\w+)', 'mobile.views.party_vote'),
    ('^party/(?P<slug>\w+)/dashboard', 'desktop.views.party_dash'),
    ('^dashboard', 'desktop.views.dashboard'),
    ('^$', 'desktop.views.index'),



    #Form Lines
    # Examples:
    # url(r'^$', 'SpunByMe.views.home', name='home'),
    # url(r'^SpunByMe/', include('SpunByMe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf here ...

urlpatterns += staticfiles_urlpatterns()