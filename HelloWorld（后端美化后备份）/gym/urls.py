from django.urls import path

from . import views

app_name = 'gym'

urlpatterns = [
    # ex: /gym/
    path('', views.index, name='index'),
]