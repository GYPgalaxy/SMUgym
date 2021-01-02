from django.urls import path

from . import views

app_name = 'gym'

urlpatterns = [
    # ex: http://localhost:8000/gym/
    path('', views.index, name='index'),

    # ex: http://localhost:8000/gym/login/
    path('login/', views.login, name='login'),

    # ex: http://localhost:8000/gym/logout/
    path('logout/', views.logout, name='logout'),

    # ex: http://localhost:8000/gym/register/
    path('register/', views.register, name='register'),

    # ex: http://localhost:8000/gym/mygxin/
    path('mygxin/', views.mygxin, name='mygxin'),

    # ex: http://localhost:8000/gym/mygrxx/
    path('mygrxx/', views.mygrxx, name='mygrxx'),

    # ex: http://localhost:8000/gym/myprod/
    path('myprod/', views.myprod, name='myprod'),

    # ex: http://localhost:8000/gym/myorderq/
    path('myorderq/', views.myorderq, name='myorderq'),

    # ex: http://localhost:8000/gym/remima/
    path('remima/', views.remima, name='remima'),

    # 测试用
    path('show/', views.showcourse, name='showcourse'),
]
