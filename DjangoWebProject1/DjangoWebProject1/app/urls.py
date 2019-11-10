from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('',views.index),
    path('index', views.index,name='主页'),
    path('wenzhang', views.wenzhang,name='文章'),
    path('biaodan/', views.biaodan,name='表单'),


    path('del/<forloop_counter>',views.delete,name='删除'),

    path('edit/',views.edit,name='修改'),
    #====================
    path('home',views.home),
    path('muban',views.muban),
    path('ii', views.ii),
    path('xx',views.xx)
    
    


]