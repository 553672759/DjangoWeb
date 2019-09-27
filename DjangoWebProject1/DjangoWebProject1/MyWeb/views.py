from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import MywebDblist,MywebVideos
#===========================
lst = [{'待办事项':'遛狗','已完成':False},
       {'待办事项':'遛猫','已完成':True},
       ]
#===========================

# Create your views here.
def index(request):
    return render(request,"MyWeb/index.html")

def wenzhang(request):
    return render(request,"MyWeb/wenzhang.html")



def xinwen(request):
    return render(request,"MyWeb/xinwen.html")

#教程 待办事项
def jiaocheng(request):
    global lst
    if request.method == "POST":
        if request.POST['待办事项']=="":
            content = {'清单':MywebDblist.objects.all(),'警告':'请输入内容'}
            return render(request,"MyWeb/jiaocheng.html",content)
        else:
            lst.append({'待办事项':request.POST['待办事项'],'已完成':False})
            #======向数据库添加数据========
            MywebDblist.objects.create(daiban=request.POST['待办事项'],yiwancheng='0')
            #==============================

            content = {'清单':MywebDblist.objects.all(),'信息':'添加成功！'}
            return render(request,"MyWeb/jiaocheng.html",content)
    else:
        content = {'清单':MywebDblist.objects.all()}
        return render(request,"MyWeb/jiaocheng.html",content)


def edit(request,one_id):
    global lst
    if request.method == "POST":
        if request.POST['new'] == '':
            return render(request,"MyWeb/bianji.html",{'警告':'请输入内容！'})
        else:
            #lst[int(forloop_counter)-1]['待办事项']=request.POST['new']
            MywebDblist.objects.filter(id=one_id).update(daiban=request.POST['new'])
            return redirect("MyWeb:教程")
    elif request.method == "GET":
        print("编辑"+one_id)
        content = { 'old' : MywebDblist.objects.get(id=one_id)}
        print(content)
        return render(request,"MyWeb/bianji.html",content);


def delete(request,one_id):  
    #lst.pop(int(forloop_counter) - 1)
    print(one_id)
    MywebDblist.objects.filter(id=str(int(one_id)-1)).delete()
    return redirect("MyWeb:教程")

def change(request,one_id):
    #lst[int(forloop_counter)-1]['已完成']= not (lst[int(forloop_counter)-1]['已完成'])
    xx = MywebDblist.objects.get(id=str(int(one_id)-1)).yiwancheng
    MywebDblist.objects.filter(id=str(int(one_id)-1)).update(yiwancheng = not xx)
    return redirect("MyWeb:教程")

def cross(request,forloop_counter):
    global lst
    if request.POST['完成状态']=='已完成':
        lst[int(forloop_counter)-1]['已完成']=True
    else:
        lst[int(forloop_counter)-1]['已完成']=False
    return redirect("MyWeb:教程")

def movie(request):
    #print(MywebVideos.objects.get(videoid='002a023d-5c0f-48f6-b388-76f8986dc69a').videotitle)
    #content = { 'movieList' : MywebVideos.objects.get(videoid='002a023d-5c0f-48f6-b388-76f8986dc69a')}
    content = { 'movieList' : MywebVideos.objects.all()[:10]}
     
    return render(request,"MyWeb/movie.html",content)
    

