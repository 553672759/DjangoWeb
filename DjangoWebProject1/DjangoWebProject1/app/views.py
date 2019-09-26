# -*- coding: utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext
from datetime import datetime


#===========================
lst = [{'待办事项':'遛狗','已完成':False},
       {'待办事项':'遛猫','已完成':True},
       ]
#===========================
def index(request):
    return render(request,"app/index.html")

def wenzhang(request):
     return render(request,"app/wenzhang.html")


def biaodan(request):
    global lst
    if request.method == "POST":
        if request.POST['待办事项']=="":
            content = {'清单':lst}
            return render(request,"app/biaodan.html",content)
        else:
            lst.append({'待办事项':request.POST['待办事项'],'已完成':False})
            #content =  {'待办事项' : str(request.POST['待办事项']) ,'是什么':'' }
            content = {'清单':lst}
            return render(request,"app/biaodan.html",content)
    else:
        content = {'清单':lst}
        return render(request,"app/biaodan.html",content)


def delete(request,fotloop_counter):    
    return redirect("app:表单")

def edit(request):
    return render(rquest,"app/edit.html");

#=======================================================
def muban(request):
    return render(request,"app/muban.html")

def ii(request):
    return render(request,"app/home.html")


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
