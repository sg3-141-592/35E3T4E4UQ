from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('about', TemplateView.as_view(template_name="base.html")),
    path('processing', TemplateView.as_view(template_name="processing.html")),
    path('processing/<int:process_id>/', views.ProcessingView.as_view(), name='processing view')
]