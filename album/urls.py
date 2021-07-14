from django.conf.urls import url 
from album import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
                       url(r'^$', views.TemplateListView.as_view(), name='template-list'),
                       url(r'^(?P<pk>\d+)/detail/$', views.TemplateDetailView.as_view(),
                           name='template-detail'),
                       # Update
                       url(r'^(?P<pk>\d+)/update/$', views.TemplateUpdate.as_view(), name='template-update'),
                       #Create
                       url(r'^create/$', views.TemplateCreate.as_view(), name='template-create'),
                       #Delete
                       url(r'^(?P<pk>\d+)/delete/$', views.TemplateDelete.as_view(), name='template-delete'),
                       
]