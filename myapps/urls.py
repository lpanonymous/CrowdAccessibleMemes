from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
# Importamos Django REST Framework y la vista 'template' 
from rest_framework import routers
from album import views

router = routers.DefaultRouter()
router.register(r'templates', views.TemplateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('album.urls')),
    path('api/', include(router.urls)),
]

