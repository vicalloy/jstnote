from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from jstnote import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='note_idx'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='note_detail'),
    url(r'^(?P<pk>\d+)/to_edit/$', views.to_edit, name='note_to_edit'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit, name='note_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete, name='note_delete'),
)
