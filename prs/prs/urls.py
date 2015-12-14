from django.conf.urls import include, url
from django.contrib import admin

import movie
import analytics
import recommender

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rec/', include('recommender.urls')),
    url(r'^log/', include('evidenceCollector.urls')),
    url(r'^analytics/', include('analytics.urls')),
    url(r'^', include('movie.urls')),
]
