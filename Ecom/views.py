from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.all()
        context['product'] =  product
        return context
    