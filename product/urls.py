
from django.contrib import admin
from django.urls import include, path
from product import views

urlpatterns = [
    
    path('addproduct/', views.addProduct),
    path('viewproduct/', views.viewproduct),
    path('productpage/', views.productpage),
]
