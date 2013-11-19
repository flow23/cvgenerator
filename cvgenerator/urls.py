from django.conf.urls import patterns, include, url, static
from django.conf import settings

from cvgenerator import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cvgenerator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Index
    url(r'^$', views.IndexView.as_view(), name="index"),


    # CV namespace
    #url(r'^cv/', include('cv.urls', namespace="cv")),

    # Employee namespace
    url(r'^employee/', include('cv.urls', namespace="employee")),

    # Generator namespace
    url(r'^generator/', include('generator.urls', namespace="generator")),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    #Media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
)
