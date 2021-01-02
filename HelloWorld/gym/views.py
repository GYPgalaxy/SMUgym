from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import User, Coach, Course, Locker, PhyTest


def index(request):
    latest_course_list = Course.objects.all()[:12]
    context = {'latest_course_list': latest_course_list}
    return render(request, 'gym/index.html', context)

def login(request):
    context = {}
    if request.method == 'POST':
        # 获取到用户提交的用户名密码
        # 1）校验成功，告知登陆成功
        # 2）校验失败，返回登陆页面
        tel = request.POST.get('tel')
        pwd = request.POST.get('pwd')
        print(tel, pwd)
        if User.objects.filter(tel=tel, pwd=pwd):
            request.session['tel'] = tel
            latest_course_list = Course.objects.all()[:12]
            context['latest_course_list'] = latest_course_list
            return redirect(reverse('gym:index'), latest_course_list=latest_course_list)
        else:
            context['msg'] = '用户名或密码错误'
    return render(request, 'gym/login.html', context)

def logout(request):
    latest_course_list = Course.objects.all()[:12]
    context = {'latest_course_list': latest_course_list}
    request.session.flush()
    return redirect(reverse('gym:index'))

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

def mygxin(request):
    tel = request.session.get('tel')
    user = User.objects.get(tel=tel)
    context = {'user': user}
    return render(request, 'gym/mygxin.html', context)

def mygrxx(request):
    tel = request.session.get('tel')
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        User.objects.filter(tel=tel).update(name=name)
        User.objects.filter(tel=tel).update(gender=gender)
    user = User.objects.get(tel=tel)
    context = {'user': user}
    return render(request, 'gym/mygrxx.html', context)
