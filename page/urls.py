from django.urls import path 
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('v/',views.PosterListView.as_view(),name='pictures'),
    path('x/', views.XPageView.as_view(), name='x-page'),
    path('pre/', views.pressureView.as_view(), name='pressure-page'),
    path('p/', views.Hassan.as_view(), name='rights-page'),
    path('R/',views.ptrights,name='pt-rights')



]
    
