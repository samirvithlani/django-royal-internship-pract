from email.headerregistry import Address
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import  AddressForm
from .models import Address

# Create your views here.
class CreateAddress(CreateView):
    form_class = AddressForm
    model = Address
    template_name = 'address/address_form.html'
    success_url = '/'
