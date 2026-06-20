from django.urls import path 
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('v/',views.PosterListView.as_view(),name='pictures'),
    path('x/', views.XPageView.as_view(), name='x-page'),
    path('pre/', views.pressureView.as_view(), name='pressure-page'),
    path('p/', views.Hassan.as_view(), name='rights-page'),
    path('R/',views.ptrights,name='pt-rights'),
    path('i/' ,views.infection,name='5 moments'),
    path('hand/' ,views.hand,name='typesofhandwash'),
    path('PE/' ,views.PPE,name='PPE'),
    path('Isolation/' ,views.iso,name='isolation'),
    path('Inject/' ,views.Inj,name='injection'),
    path('utilization/' ,views.U,name='uti'),
    path('O/' ,views.out,name='النفايات'),
    path('V/' ,views.vap,name='vbundle'),
    path('po/' ,views.test,name='t'),
    path('check/' ,views.gahar_checklist_view,name='list'),
    path('gahar-arabic/' ,views.g,name='pdf'),
    path('gahar-eng;ish/' ,views.gahar,name='pdf2'),

   







]
    
