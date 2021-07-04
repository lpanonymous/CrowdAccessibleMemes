from rest_framework import serializers
from album.models import Template, Meme
 
class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'name', 'template', 'pub_date', 'context']
        extra_kwargs = {'id': {'required': False}}

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ['id', 'template', 'meme', 'pub_date']
        extra_kwargs = {'id': {'required': False}}