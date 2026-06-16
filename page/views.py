from django.shortcuts import render
from django.views.generic import TemplateView
#from django.http import HttpResponse
# Create your views here.

from django.views.generic import ListView , DetailView

from .models import Poster
from .models import StaticPage


class PosterListView(ListView):
    model = Poster
    template_name = 'hassan/poster.html'
    context_object_name = 'posters'

class HomeView(TemplateView):
    template_name = 'hassan/home.html'

class XPageView(TemplateView):
    template_name = 'hassan/x.html'

class pressureView(ListView):
    model = StaticPage
    template_name = 'hassan/pressure_ulcer.html'
    context_object_name = 'pressure'  


class Hassan(TemplateView):
  
    template_name = 'hassan/poster1.html'
    context_object_name = 'معايير السلامه' 

def ptrights(request):
    return render(request,'hassan/pt_rights.html',)

