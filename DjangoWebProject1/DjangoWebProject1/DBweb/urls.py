from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf.urls import url

app_name = 'DBweb'
urlpatterns = [
    url('index',views.index,name='主页'),
    url('admin', admin.site.urls),
    url('base', views.base),
    url('FWFL',views.FWFL), #服务分类
    url('JXPL',views.JXPL), #精选评论
    url('JXYD',views.JXYD), #精选优店
    url('YJTS',views.YJTS), #意见投诉
    

]