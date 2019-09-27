from django.urls import path,include
from django.contrib import admin
from MyWeb import views

app_name = 'MyWeb'
urlpatterns = [
    path('',views.index,name='主页'),
                                           
    path('wenzhang',views.wenzhang,name='文章'),
    path('jiaocheng',views.jiaocheng,name='教程'),
    path('xinwen',views.xinwen,name='新闻'),

    path('movie',views.movie,name='电影'),
    path('lianjie',views.lianjie,name='链接'),

    path('del/<one_id>',views.delete,name='删除'),
    path('edit/<one_id>',views.edit,name='编辑'),
    path('change/<forloop_counter>',views.change,name='改变'),
    path('huadiao/<forloop_counter>',views.cross,name='划掉'),


]           