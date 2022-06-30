
from django.contrib import admin
from django.urls import include, path
from .views import  ProductDetailView
from .views import ProductListView

urlpatterns = [

    path('productlist/', ProductListView.as_view(), name='product_list'),
    path('productlist/<int:pk>/', ProductDetailView.as_view(), name='product_list'),

]
