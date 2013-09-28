from django.conf.urls import patterns, include, url
from suggestionbox import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^addSuggestion/$', views.addSuggestion, name='addSuggestion'),
    url(r'^detail/(?P<suggestion_id>\d+)/$', views.detail, name='detail'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
