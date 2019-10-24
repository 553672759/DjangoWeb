from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    url(r'^admin', admin.site.urls),

   

]