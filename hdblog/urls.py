from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hdyazi.views.home', name='home'),
	
	url(r'^blog/$', 'hdyazi.views.yazi', name='yazi'),
	url(r'^(?P<slug>.*).html$', 'hdyazi.views.post', name='post'),
	url(r'^blog/etiket/(?P<tag_name>.*)/$', 'hdyazi.views.etiket', name='etiket'),
	url(r'^blog/kategori/(?P<slug>.*)/$', 'hdyazi.views.kategori', name='kategori'),

	url(r'^makaleler/$', 'hdyazi.views.makaleler', name='makaleler'),
	url(r'^makale/(?P<kat_slug>.*)/(?P<slug>.*)/$', 'hdyazi.views.makale', name='makale'),
	url(r'^makale/(?P<kat_slug>.*)/$', 'hdyazi.views.mkategori', name='mkategori'),		
	url(r'^makaleler/(?P<tag_name>.*)/$', 'hdyazi.views.metiket', name='metiket'),

    # url(r'^hdblog/', include('hdblog.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:\Users\DELL\Desktop\hdblog\media'}),
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:\Users\DELL\Desktop\hdblog\hdblog\static'}),
    )