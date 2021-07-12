from django.db import models
from django.db.models.signals import post_delete
from django.urls import reverse
from django.dispatch import receiver
from django.utils.html import mark_safe
from os.path import join as osjoin

class Template(models.Model):
    """ Plantillas del album """
    name = models.CharField(max_length=100, verbose_name="Nombre")
    template = models.ImageField(upload_to='templates/', verbose_name="Plantilla")
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
            return mark_safe('<img src="/static{}" width="300" height="300" />'.format(self.template.url))
        return ""

class Meme(models.Model):
    """ Fotos del album """

    def image_dir(self, filename):
        return 'memes/'+osjoin(str(self.template.name), filename)

    template = models.ForeignKey(Template, on_delete=models.CASCADE,null=True, blank=True, verbose_name="Template")
    meme = models.ImageField(upload_to=image_dir, verbose_name="Meme")
    pub_date = models.DateField(auto_now_add=True)
     
    class Meta:
        verbose_name = "meme"
        verbose_name_plural = "memes"

    def __str__(self):
        return self.template.name  # <=====

    def __unicode__(self):
        return self.template

    def get_absolute_url(self):
        return reverse('meme-list')

    @property
    def meme_preview(self):
        if self.meme:
            return mark_safe('<img src="/static{}" width="300" height="300" />'.format(self.meme.url))
        return ""

