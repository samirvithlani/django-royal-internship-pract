from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# Create your views here.

def group(request):
    return HttpResponse("group called...")

def index(request):
    context ={
        'name':'FLIPKART',
    }
    return render(request, 'group/index.html',context)

def contactUs(request):
    context   = {
        'contact_name':["Dhiraj","Vinod","Rajesh","Suresh","Sachin"]
    }
    return render(request, 'group/contactUs.html',context)

def aboutus(request):
    context = {
        'isActive':True,
        'age':2,
    }
    return render(request, 'group/aboutus.html',context)

