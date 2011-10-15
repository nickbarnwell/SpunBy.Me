from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^search/', 'common.views.search'),
    ('^add_song/', 'common.views.add_song'),
    ('^party/(?P<slug>\w+)/', 'desktop.views.party'),
    ('^login/', 'desktop.views.login'),
    ('', 'desktop.views.index'),
    # Examples:
    # url(r'^$', 'SpunByMe.views.home', name='home'),
    # url(r'^SpunByMe/', include('SpunByMe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
