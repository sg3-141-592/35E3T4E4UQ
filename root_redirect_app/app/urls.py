from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about', TemplateView.as_view(template_name="base.html")),
    path('processing', TemplateView.as_view(template_name="processing.html")),
]