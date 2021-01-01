from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import User, Coach, Course, Locker, PhyTest
# Create your views here.
def index(request):
    return HttpResponse("You're looking at gym.")