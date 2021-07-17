from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
# Importamos Django REST Framework y la vista 'template' 
from rest_framework import routers
from album import views
from django.config import settings
from django.config.urls.static import static 

router = routers.DefaultRouter()
router.register(r'templates', views.TemplateViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('album.urls')),
    path('api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

