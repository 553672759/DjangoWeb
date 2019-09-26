from django.urls import path,include
from app import urls
from MyWeb import  urls
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('MyWeb.urls')),
]