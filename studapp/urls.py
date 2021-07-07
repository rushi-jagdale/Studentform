from django.urls import path
from . import views

urlpatterns = [
    path('',views.show,name='show'),
    path('add/',views.add,name='add'),
        
]
