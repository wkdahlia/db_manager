from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

import time


# def timer(request):
#     return HttpResponse(time.time())
#
#
# def my_login(request):
#     return render(request, "login.html")
#
#
# def my_auth(request):
#     return HttpResponse("登陆成功")
from myweb import models


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = models.UserInfo.objects.filter(user=username,pwd=password).first()
        if user:
            return redirect('http://www.baidu.com')
        # if username == 'alex' and password == '123':
        #     return redirect('http://www.baidu.com')
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误'})


def index(request):
    # return HttpResponse('欢迎登陆')
    return render(request,'index.html')


# def test(request):
#     user_list = models.UserInfo.objects.all()
#     for obj in user_list:
#         print(obj,obj.user,obj.pwd,obj.age)
#
#     user_list = models.UserInfo.objects.filter(user='alex',pwd='123').all()
#     user = models.UserInfo.objects.filter(user='alex',pwd='123').first()


def parts(request):
    depart_list = models.Department.objects.all()
    paginator = Paginator(depart_list, 10)
    page = request.GET.get('page')
    try:
        hosts_page = paginator.page(page)
    except PageNotAnInteger:
        hosts_page = paginator.page(1)
    except EmptyPage:
        hosts_page = paginator.page(paginator.num_pages)
    return render(request,'parts.html',{'cur_list':hosts_page})


def parts_add(request):
    if request.method == 'GET':
        return render(request,'parts_add.html')
    else:
        ti = request.POST.get('title')
        models.Department.objects.create(title=ti)
        return redirect('/myweb/parts/')
        #方法2
        # obj = models.Department(title=ti)
        # obj.save()


def part_del(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/myweb/parts/')


def part_edit(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Department.objects.filter(id=nid).first()
        if not obj:
            return HttpResponse('输入有误')
        return render(request,'part_edit.html',{'obj':obj})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        models.Department.objects.filter(id=nid).update(title=title)
        return redirect('/myweb/parts/')


def hosts(request):
    hosts_list = models.Hosts.objects.all()
    paginator = Paginator(hosts_list,10)
    page = request.GET.get('page')
    try:
        hosts_page = paginator.page(page)
    except PageNotAnInteger:
        hosts_page = paginator.page(1)
    except EmptyPage:
        hosts_page = paginator.page(paginator.num_pages)
    return render(request, 'hosts.html', {'cur_list': hosts_page})


def hosts_del(request):
    nid = request.GET.get('nid')
    models.Hosts.objects.filter(id=nid).delete()
    return redirect('/myweb/hosts/')


def hosts_edit(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Hosts.objects.filter(id=nid).first()
        depart_list = models.Department.objects.all()
        if not obj:
            return HttpResponse('输入有误')
        return render(request,'hosts_edit.html',{'obj':obj,'depart_list':depart_list})
    else:
        nid = request.GET.get('nid')
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        depart = request.POST.get('depart')
        depart_list = models.Department.objects.filter(title=depart)
        models.Hosts.objects.filter(id=nid).update(hostname=hostname,ip=ip,depart=depart_list[0])
        return redirect('/myweb/hosts/')


def hosts_add(request):
    if request.method == 'GET':
        depart_list = models.Department.objects.all()
        return render(request,'hosts_add.html',{'depart_list':depart_list})
    else:
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        depart = request.POST.get('depart')
        depart_list = models.Department.objects.filter(title=depart)
        models.Hosts.objects.create(hostname=hostname,ip = ip,depart=depart_list[0])
        return redirect('/myweb/hosts/')


def users_list(request):
    users_list = models.UserInfo.objects.all()
    paginator = Paginator(users_list, 10)
    page = request.GET.get('page')
    try:
        hosts_page = paginator.page(page)
    except PageNotAnInteger:
        hosts_page = paginator.page(1)
    except EmptyPage:
        hosts_page = paginator.page(paginator.num_pages)
    return render(request, 'users.html', {'cur_list': hosts_page})



def users_add(request):
    if request.method == "GET":
        return render(request,'users_add.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = request.POST.get('age')
        models.UserInfo.objects.create(user=username, pwd=password, age=age)
        return redirect('/myweb/users/')


def users_del(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/myweb/users/')


def users_edit(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.UserInfo.objects.filter(id=nid).first()
        if not obj:
            return HttpResponse('输入有误')
        return render(request,'users_edit.html',{'obj':obj})
    else:
        nid = request.GET.get('nid')
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = request.POST.get('age')
        models.UserInfo.objects.filter(id=nid).update(user=username, pwd=password, age=age)
        return redirect('/myweb/users/')