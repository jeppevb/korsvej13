from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'booking.views.home', name='home'),
    url(r'^book[/]?$', 'booking.views.book', name='book'),
    url(r'^booking/([0-9]+)/([0-9]+)[/]?$', 'booking.views.booking', name='booking'),
    # url(r'^korsvej13/', include('korsvej13.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
