
from django.contrib import admin  
from django.urls import path , include 

admin.site.site_header = "ASEAN TAX Admin"
admin.site.site_title = "ASEAN TAX"
admin.site.index_title = "Welcome to ASEAN TAX"
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('log.urls'))

]
