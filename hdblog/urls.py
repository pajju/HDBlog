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
	
	url(r'^sayfa/(?P<slug>.*)/$', 'hdyazi.views.sayfalar', name='sayfalar'),
	
	url(r'^dosyalar/$', 'hdyazi.views.dosyalar', name='dosyalar'),
	url(r'^dosya/(?P<slug>.*)/$', 'hdyazi.views.dosya', name='dosya'),
	
	url(r'^link/$', 'hdlink.views.linkolustur'),
    url(r'^link/(?P<id>\w+)/$', 'hdlink.views.link'),
    url(r'^link/(?P<id>\w+)/stats$', 'hdlink.views.stats'),
	
	url(r'^duyuru/(?P<slug>.*)/$', 'hdyazi.views.duyuru', name='duyuru'),
	
	url(r'^tanitim/(?P<slug>.*)/$', 'hdyazi.views.tanitim', name='tanitim'),

    # url(r'^hdblog/', include('hdblog.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:\Users\DELL\Desktop\hdblog\media'}),
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:\Users\DELL\Desktop\hdblog\hdblog\static'}),
    )