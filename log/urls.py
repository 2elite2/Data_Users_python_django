from django.contrib import admin  
from django.urls import path  
from log import views 

urlpatterns = [  
     
      
    path('',views.index),
    path('login/',views.login),
    path('home/',views.home),
    path('select/',views.select),

]  