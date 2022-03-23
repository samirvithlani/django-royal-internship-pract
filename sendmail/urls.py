from django.contrib import admin
from django.urls import include, path
from sendmail import views

urlpatterns = [
    path('',views.sendmail,name='send_mail'),
    path('pie/',views.pie_chart,name='pie_chart'),
    
]