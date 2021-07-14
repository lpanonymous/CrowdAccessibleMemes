from rest_framework import serializers
from album.models import Template
 
class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'name', 'template', 'pub_date', 'context']
        extra_kwargs = {'id': {'required': False}}