from django.conf.urls.defaults import *
from core.views import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()
#urlpatterns = patterns('',(r'^$', homepage, {'template': 'index.html'}),
urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
    # Example:
    # (r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT }),
    )

