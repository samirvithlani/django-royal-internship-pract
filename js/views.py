from django.shortcuts import render
from django.template import context
from django.views.generic import ListView, DetailView
from .models import Product_1

# Create your views here.
class ProductListView(ListView):

    def get_queryset(self):
        products = Product_1.objects.all()
        print(products)
        return products
        
    template_name = 'js/ProductList.html'        


class ProductDetailView(DetailView):
    model = Product_1
    template_name = 'js/ProductList.html'