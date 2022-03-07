from sre_constants import SUCCESS
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from .forms import UserForm


# Create your views here.

class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'userportal/registration.html'
    success_url ="/userportal/login/"
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)  
        user.save()    
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " - User Created Successfully..!!"

    