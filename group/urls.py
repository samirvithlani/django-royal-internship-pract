from django.urls import include, path
from group import views

urlpatterns = [
   
    path('add/', views.group),
    path('contactUs/', views.contactUs),
    path('aboutus/', views.aboutus),
    path('', views.index),
]
