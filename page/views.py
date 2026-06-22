from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView , DetailView
from .models import Poster 
from .models import StaticPage
from django.contrib.auth.decorators import login_required
from .forms import ChecklistForm
from django.contrib import messages
#from django.http import HttpResponse


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

def infection(request):
    return render(request,'hassan/5 moments.html',)


def hand(request):
    return render(request,'hassan/hand-wash.html',)

def PPE(request):
    return render(request,'hassan/PPE.html',)


def iso(request):
    return render(request,'hassan/isolation.html',)


def Inj(request):
    return render(request,'hassan/injection.html',)

def U(request):
    return render(request,'hassan/utilization.html',)

def out(request):
    return render(request,'hassan/out.html',)

def vap(request):
    return render(request,'bundles/vap.html',)

def dama(request):
    return render(request,'test/DAMA.html',)


def escape(request):
    return render(request,'test/escape.html',)


def g(request):
    return render(request,'test/gahar_ar.html',)

def gahar(request):
    return render(request,'test/gahar.html',)

def entry(request):
    return render(request,'test/entrance.html',)

def verbal_order(request):
    return render(request,'test/verbal-order.html',)

def consent(request):
    return render(request,'test/consent.html',)

def con(request):
    return render(request,'test/place.html',)

def I(request):
    return render(request,'test/information.html',)

def bedsores(request):
    return render(request,'test/bed_sores.html',)

def test(request):
    return render(request,'test/test.html',)








@login_required
def gahar_checklist_view(request):
    if request.method == 'POST':
        form = ChecklistForm(request.POST)
        if form.is_valid():
            checklist = form.save(commit=False)
            checklist.inspector = request.user # حفظ المستخدم الحالي كمراجع
            checklist.save()
            messages.success(request, 'تم حفظ قائمة التحقق بنجاح!')
            return redirect('home')
    else:
        form = ChecklistForm()
    
    return render(request, 'test/checklist.html', {'form': form})









