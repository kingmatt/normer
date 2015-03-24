from django.conf.urls import patterns, url

urlpatterns = patterns('ratings.views',
    url(r'question/(?P<image_id>\d+)$', 'question', name='question'),
    url(r'thanks$', 'thanks', name='thanks'),
    url(r'^$', 'index', name='index'),
) 
