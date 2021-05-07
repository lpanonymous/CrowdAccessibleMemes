from django.conf.urls import url 
from album import views


urlpatterns = [ 
                       url(r'^$', views.base, name='base'),
                       url(r'^template/$', views.TemplateListView.as_view(), name='template-list'),
                       url(r'^template/(?P<pk>\d+)/detail/$', views.TemplateDetailView.as_view(),
                           name='template-detail'),
                       # Update
                       url(r'^template/(?P<pk>\d+)/update/$', views.TemplateUpdate.as_view(), name='template-update'),
                       #Create
                       url(r'^template/create/$', views.TemplateCreate.as_view(), name='template-create'),
                       #Delete
                       url(r'^template/(?P<pk>\d+)/delete/$', views.TemplateDelete.as_view(), name='template-delete'),
                       url(r'^meme/$', views.MemeListView.as_view(), name='meme-list'),
                       url(r'^meme/(?P<pk>\d+)/detail/$', views.MemeDetailView.as_view(),
                           name='meme-detail'),
                       # Update
                       url(r'^meme/(?P<pk>\d+)/update/$', views.MemeUpdate.as_view(), name='meme-update'),
                       #Create
                       url(r'^meme/create/$', views.MemeCreate.as_view(), name='meme-create'),
                       #Delete
                       url(r'^meme/(?P<pk>\d+)/delete/$', views.MemeDelete.as_view(), name='meme-delete'),
]