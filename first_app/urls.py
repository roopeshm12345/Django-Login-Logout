from django.shortcuts import render
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

# Create your views here.
urlpatterns=[
path('accounts/', include('django.contrib.auth.urls')),
path('', TemplateView.as_view(template_name='home.html'), name='home' ),
]
