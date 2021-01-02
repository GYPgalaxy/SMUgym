from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import User, Coach, Course, Locker, PhyTest
# Create your views here.

# 首页
def index(request):
    return render(request, 'gym/index.html')


#登录
def login(request):
    context = {}
    if request.method == 'POST':
        # 获取到用户提交的用户名密码
        # 1）校验成功，告知登陆成功
        # 2）校验失败，返回登陆页面
        tel = request.POST.get('tel')
        pwd = request.POST.get('pwd')
        if User.objects.filter(tel=tel, pwd=pwd):
            return HttpResponse('登录成功')
        else:
            context['msg'] = '用户名或密码错误'
    return render(request, 'gym/login.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        # 获取到用户提交的用户名密码
        # 1）校验成功，告知注册成功
        # 2）校验失败，返回注册页面
        tel = request.POST.get('tel')
        pwd = request.POST.get('pwd')
        if User.objects.filter(tel=tel):
            context['msg'] = '该用户已被注册'
        else:
            newuser = User(tel=tel, pwd=pwd)
            newuser.save()
            context['msg'] = '注册成功'
    return render(request, 'gym/register.html', context)