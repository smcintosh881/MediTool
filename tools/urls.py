from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^appointment/$', views.CreateAppointment.as_view(success_url="/"), name='appointment'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^(?P<tool_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.CreatePatient.as_view(success_url="/"), name='create'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.EditPatient.as_view(success_url="/"), name='edit')
]
