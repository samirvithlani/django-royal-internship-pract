from os import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'product_urls'

urlpatterns = [
    
    path("user-login/",BaseRegisterView.as_view(),name="user-registration"),
    path('login/', LoginView.as_view(template_name='userportal/login.html', success_url = '/UserApp/'), name='user-login'),
    
]
