from django.contrib import admin
from album.models import Template

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'context')
    list_editable = ["context"]
    search_fields = ["name"]
    readonly_fields = ('template_preview',)

    def template_preview(self, obj):
        return obj.template_preview

    template_preview.short_description = 'Template Preview'
    template_preview.allow_tags = True

admin.site.register(Template, TemplateAdmin)
