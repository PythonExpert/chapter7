from django.conf.urls import patterns, url, include
from analytics import views

urlpatterns = patterns('',
	url(r'^api/get_statistics', views.get_statistics, name='get statistics'),
	url(r'^api/events_on_conversions', views.events_on_conversions, name='events_on_conversions'),
	url(r'^api/top_content_by_eventtype', views.top_content_by_eventtype, name='top_content_by_eventtype'),
	url(r'^api/top_content', views.top_content, name='top_content'),	
	url(r'^api/user_evidence/(?P<userid>[a-zA-Z0-9]+)', views.user_evidence, name='user_evidence'),	
	url(r'^dashboard', views.dashboard, name='dashboard'),


	url(r'^api/get_user_statistics/(?P<userid>[a-zA-Z0-9]+)', views.get_user_statistics, name='get_user_statistics'),	

	url(r'^user/(?P<userid>[a-zA-Z0-9]+)', views.user, name='user'),
	)
    