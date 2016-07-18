import core.views

from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),

	url(r'^layer/(?P<slug>[a-z0-9\-\_]+)/$', core.views.layer),
	url(r'^$', core.views.index)
]

if settings.DEBUG:
	urlpatterns.append(
		url(
			r'^media/(?P<path>.*)$', serve,
			{'document_root': settings.MEDIA_ROOT}
		),
	)
