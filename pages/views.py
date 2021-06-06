from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """View for home page."""
    template_name = 'home.html'