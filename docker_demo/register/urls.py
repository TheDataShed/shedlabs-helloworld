from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.attendee_list, name='attendee_list'),
    url(r'^attendee/(?P<pk>\d+)/$', views.attendee_detail, name='attendee_detail'),
    url(r'^attendee/new/$', views.attendee_new, name='attendee_new'),
]