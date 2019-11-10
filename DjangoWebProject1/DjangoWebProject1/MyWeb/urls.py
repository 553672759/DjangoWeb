from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin
from MyWeb import views

app_name = 'MyWeb'
urlpatterns = [
    path('',views.index,name='主页'),
    path('lay',views.layout),                                       
    path('wenzhang',views.wenzhang,name='文章'),
    path('jiaocheng',views.jiaocheng,name='教程'),
    path('xinwen',views.xinwen,name='新闻'),

    path('movie',views.movie,name='电影'),
    path('lianjie/<theone_videoid>',views.lianjie,name='链接'),

    path('del/<one_id>',views.delete,name='删除'),
    path('edit/<one_id>',views.edit,name='编辑'),
    path('change/<forloop_counter>',views.change,name='改变'),
    path('huadiao/<forloop_counter>',views.cross,name='划掉'),

    url(r'^login.html$',views.Login.as_view()),
    #路由系统
    url(r'^laoindex/',views.laoindex),
    #动态路由
    url(r'^laoedit/(\w+)',views.laoedit),
    url(r'^laoedit$/(?P<a1>\w+)/(?P<a2>\w+)',views.laoedit2),
    url(r'^err',views.err),
    #路由分发
    url(r'^app/',include('app.urls'))


]           