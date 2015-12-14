from django.conf.urls import patterns, url, include
from django.conf.urls import patterns, url, include

from evidenceCollector import views

urlpatterns = patterns('',
	url ( r'^(?P<contentid>[a-zA-Z0-9]+)/(?P<event>[a-zA-Z:0-9]+)$' ,  views.index , name = 'index' ),
)
    