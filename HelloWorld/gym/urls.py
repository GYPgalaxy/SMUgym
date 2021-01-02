from django.urls import path

from . import views

# app_name = 'gym'

urlpatterns = [
    # ex: http://localhost:8000/gym/
    path('', views.index, name='index'),

    # ex: http://localhost:8000/gym/login/
    path('login/', views.login, name='login'),

    # ex: http://localhost:8000/gym/register/
    path('register/', views.register, name='register'),
]