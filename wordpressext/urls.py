from django.conf.urls import patterns, url

urlpatterns = patterns('wordpressext.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.+)/disqus/$', 'disqus', name='wp_disqus'),
)
