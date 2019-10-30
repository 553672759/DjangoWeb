from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,"DBweb/login.html")

def base(request):
    return render(request,"DBweb/base.html")

def index(request):
    return render(request,"DBweb/index.html")

#服务分类
def FWFL(request):
    return render(request,"DBweb/FWFL.html")

#精选评论
def JXPL(request):
    return render(request,"DBweb/JXPL.html")

#精选优店
def JXYD(request):
    return render(request,"DBweb/JXYD.html")

#意见投诉
def YJTS(request):
    return render(request,"DBweb/YJTS.html")