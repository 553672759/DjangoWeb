from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"DBweb/login.html")

def base(request):
    return render(request,"DBweb/base.html")

def index(request):
    return render(request,"DBweb/index.html")