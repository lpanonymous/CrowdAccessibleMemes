from django.contrib import admin
from album.models import Template
from album.models import Meme

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'context')
    list_editable = ["context"]
    search_fields = ["name"]
    readonly_fields = ('template_preview',)

    def template_preview(self, obj):
        return obj.template_preview

    template_preview.short_description = 'Template Preview'
    template_preview.allow_tags = True

class MemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'template', 'meme')
    readonly_fields = ('meme_preview',)

    def meme_preview(self, obj):
        return obj.meme_preview

    meme_preview.short_description = 'Template Preview'
    meme_preview.allow_tags = True

admin.site.register(Template, TemplateAdmin)
admin.site.register(Meme, MemeAdmin)

