from django.conf.urls import patterns, url

from cv import views

urlpatterns = patterns('',
    # Example: /employee/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Example: /employee/1/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # Example: /employee/1/generate_form
    url(r'^(?P<pk>\d+)/update$', views.UpdateView.as_view(), name='update'),
    # Example: /employee/1/generate_form
    url(r'^(?P<pk>\d+)/generate_form$', views.DetailView.as_view(), name='generate_form'),
)
