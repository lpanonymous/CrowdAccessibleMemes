from django.db import models
from django.db.models.signals import post_delete
from django.urls import reverse
from django.dispatch import receiver
from django.utils.html import mark_safe
from os.path import join as osjoin

from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission
permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.OWNER,
   GoogleDrivePermissionType.USER,
   "lpanonymous0101@gmail.com"
)

# Define Google Drive Storage
gd_storage = GoogleDriveStorage(permissions=(permission,))

class Template(models.Model):
    """ Plantillas del album """
    name = models.CharField(max_length=100, verbose_name="Nombre")
    template = models.ImageField(upload_to='templates/', verbose_name="Plantilla", storage=gd_storage)
    pub_date = models.DateField(auto_now_add=True)
    context = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Contexto")
     
    class Meta:
        verbose_name = "plantilla"
        verbose_name_plural = "plantillas"

    def get_absolute_url(self):
        return reverse('template-list')
    
    def __str__(self):
        return self.name

    @property
    def template_preview(self):
        if self.template:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.template.url))
        return ""

