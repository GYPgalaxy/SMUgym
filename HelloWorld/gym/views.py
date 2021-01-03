from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import User, Coach, Course, Locker, PhyTest, Order, Message


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

def myorderq(request):
    tel = request.session.get('tel')
    user = User.objects.get(tel=tel)
    context = {'user': user}
    order_list = Order.objects.filter(user_id=user.id)
    for order in order_list:
        order.course_id = Course.objects.get(id=order.course_id)
    context['order_list'] = order_list
    return render(request, 'gym/myorderq.html', context)

def myprod(request):
    tel = request.session.get('tel')
    user = User.objects.get(tel=tel)
    context = {'user': user}
    order_list = Order.objects.filter(user_id=user.id)
    for order in order_list:
        order.course_id = Course.objects.get(id=order.course_id)
        context['fake_comment'] = order.comment
    context['order_list'] = order_list
    if request.method == 'POST':
        comment = request.POST.get('comment')
        print(comment)
        Order.objects.filter(user_id=user.id).update(comment=comment)
        Order.objects.filter(user_id=user.id).update(star=5)
        Order.objects.filter(user_id=user.id).update(status=1)
    return render(request, 'gym/myprod.html', context)

def remima(request):
    tel = request.session.get('tel')
    user = User.objects.get(tel=tel)
    context = {'user': user}
    if request.method == 'POST':
        pwd = request.POST.get('pwd')
        new_pwd = request.POST.get('new_pwd')
        new_pwd_1 = request.POST.get('anew_pwd')
        print(new_pwd, new_pwd_1)
        if User.objects.filter(tel=tel, pwd=pwd):
            if new_pwd == new_pwd_1:
                User.objects.filter(tel=tel, pwd=pwd).update(pwd=new_pwd)
                context['msg'] = '修改成功'
            else:
                context['msg'] = '两次密码不匹配'
        else:
            context['msg'] = '原密码错误'
    return render(request, 'gym/remima.html', context)

def showcourse(request):
    tel = request.session.get('tel')
    user = User.objects.get(tel=tel)
    context = {'user': user}
    course_list = Course.objects.all()
    context['course_list'] = course_list
    return render(request, 'gym/showcourse.html', context)

def orderxq(request, order_id):
    tel = request.session.get('tel')
    user = User.objects.get(tel=tel)
    context = {'user': user}
    order = Order.objects.get(id=order_id)
    course = Course.objects.get(id=order.course_id)
    coach = Coach.objects.get(id=course.coach_id)
    context['order'] = order
    context['course'] = course
    context['coach'] = coach
    return render(request, 'gym/orderxq.html', context)

#支付成功
def ok(request):
    return render(request,'gym/ok.html')
#展示教练
def showcoach(request):
    return render(request,'gym/showcoach.html')
#订单
def order(request):
    return render(request,'gym/order.html')
#储物柜
def locker(request):
    return render(request,'gym/locker.html')

