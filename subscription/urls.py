from django.conf.urls.defaults import *

urlpatterns = patterns('subscription.views',
    url(r'^$', 'subscribe', name='subscribe'),
    route(r'^(\d+)/sucesso/$', GET='new', POST='create', name='success'),
)

