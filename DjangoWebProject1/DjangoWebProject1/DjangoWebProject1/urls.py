from django.urls import path,include
from app import urls
from MyWeb import  urls
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('MyWeb.urls')), #引用其他URLconfs
    #path()有四个参数 route和view，可选参数kwargs和name.
    #参数route 仅匹配//中的,不会匹配GET和POST参数


]