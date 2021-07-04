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
                       url(r'^meme/$', views.MemeListView.as_view(), name='meme-list'),
                       url(r'^meme/(?P<pk>\d+)/detail/$', views.MemeDetailView.as_view(),
                           name='meme-detail'),
                       # Update
                       url(r'^meme/(?P<pk>\d+)/update/$', views.MemeUpdate.as_view(), name='meme-update'),
                       #Create
                       url(r'^meme/create/$', views.MemeCreate.as_view(), name='meme-create'),
                       #Delete
                       url(r'^meme/(?P<pk>\d+)/delete/$', views.MemeDelete.as_view(), name='meme-delete'),
                       
                       url(r'^login/$', auth_views.LoginView.as_view(template_name="auth/login.html", redirect_authenticated_user=True), name='auth_login'),
]