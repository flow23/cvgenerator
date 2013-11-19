from django.conf.urls import patterns, url

from generator import views

urlpatterns = patterns('',
    # Example: /generator/
    url(r'^$', views.GeneratorIndexView.as_view(), name='index'),
    # Example: /generator/create/
    url(r'^create/$', views.GeneratorCreateView.as_view(), name='create'),
    # Example: /generator/create/1
    url(r'^create/(?P<employee>\d+)/$', views.GeneratorCreateView.as_view(), name='create'),
    # Example: /generator/1
    url(r'^(?P<pk>\d+)/$', views.GeneratorDetailView.as_view(), name='detail'),
)
