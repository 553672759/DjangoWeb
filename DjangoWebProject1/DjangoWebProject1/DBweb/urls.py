from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    #url(r'',views.login),
    url(r'^admin', admin.site.urls),
    url(r'base', views.base),
    url('',views.index),
    
   

]