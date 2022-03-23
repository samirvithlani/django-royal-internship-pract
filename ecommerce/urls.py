"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('product.urls')),
    path('group/',include('group.urls')),
    path('orm/',include('orm.urls')),
    path('employee/',include('employee.urls')),
    path('cbv/',include('cbv.urls')),
    path('task/',include('Task.urls')),
    path('ticket/',include('ticket.urls')),
    path('exam/',include('exam.urls')),
    path('serviceprovider/',include('serviceprovider.urls')),
    path('core/',include('core.urls')),
    path('cart/',include('cart.urls')),
    path('simpleform/',include('simpleform.urls')),
    path('user/',include('UserApp.urls')),
    path('sendmail/',include('sendmail.urls')),


]
