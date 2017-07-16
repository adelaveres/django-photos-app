# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Photo

class IndexView(generic.ListView):
    template_name = 'photos/index.html'
    context_object_name = 'photos_list'

    def get_queryset(self):
        return Photo.objects.all()[:10]

class DetailView(generic.DetailView):
    model = Photo
    template_name = 'photos/detail.html'

