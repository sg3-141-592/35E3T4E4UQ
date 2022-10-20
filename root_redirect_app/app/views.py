from django.shortcuts import render
from django.views.generic import DetailView
from .models import Site

class ProcessingView(DetailView):
    model = Site
    template_name = "processing.html"
    slug_field = 'id'
    slug_url_kwarg = 'process_id'
    context_object_name = 'site'
    
