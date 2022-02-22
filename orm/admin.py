from django.contrib import admin
from .models import Customer, Order, Product, Role, Employee,Student

# Register your models here.
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
