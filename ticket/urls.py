


from django.urls import include, path
from .views import CreateTicekt


urlpatterns = [

    path('add/', CreateTicekt.as_view())
    #path('view/', ),
    
]
