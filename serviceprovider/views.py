from django.forms import models
from django.shortcuts import render
from django.template import context
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import ServiceProvider

# Create your views here.
class AddServiceProvider(CreateView):
    model = ServiceProvider
    fields = ['name', 'address', 'email', 'phone', 'website', 'description']
    template_name = 'serviceprovider/add_serviceprovider.html'
    success_url = '/serviceprovider/view'

class ViewServiceProvider(ListView):
    model = ServiceProvider
    serviceproviders = model.objects.all()
    context_object_name = 'serviceproviders'
    template_name = 'serviceprovider/view_serviceprovider.html'    

class DetailServiceProvider(DetailView):
    model = ServiceProvider
    context_object_name = 'serviceprovider'
    template_name = 'serviceprovider/detail_serviceprovider.html'

class DeleteServiceProvider(DeleteView):
    model = ServiceProvider
    template_name = "serviceprovider/delete.html"
    success_url = '/serviceprovider/view'


class UpdateServiceProvider(UpdateView):
    model = ServiceProvider
    fields = ['name', 'address', 'email', 'phone', 'website', 'description']
    template_name = 'serviceprovider/update_serviceprovider.html'
    success_url = '/serviceprovider/view'

        

