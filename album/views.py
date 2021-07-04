from django.shortcuts import render
from album.models import Template, Meme
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
import pyttsx3
import speech_recognition as sr
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

# Clase 'TemplatesSerializer' 
from album.serializers import TemplateSerializer, MemeSerializer

def base(request):
    return render(request, 'base.html')
    
class TemplateListView(ListView):
    model = Template


class TemplateDetailView(DetailView):
    model = Template


class TemplateUpdate(UpdateView):
    model = Template
    fields = '__all__'

class TemplateCreate(CreateView):
    model = Template
    fields = '__all__'


class TemplateDelete(DeleteView):
    model = Template
    success_url = reverse_lazy('template-list')

class MemeListView(ListView):
    model = Meme


class MemeDetailView(DetailView):
    model = Meme


class MemeUpdate(UpdateView):
    model = Meme
    fields = '__all__'

class MemeCreate(CreateView):
    model = Meme
    fields = '__all__'


class MemeDelete(DeleteView):
    model = Meme
    success_url = reverse_lazy('meme-list')

class TemplateViewSet(viewsets.ModelViewSet):    
    
    queryset = Template.objects.all().order_by('id')
    serializer_class = TemplateSerializer
