from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tool_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.CreateTool.as_view(success_url="/"), name='create'),
    url(r'^edit/__FILL_ME_IN__/$', views.__FILL_ME_IN__.as_view(success_url="__FILL_ME_IN__"), name='edit')
]
