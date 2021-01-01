from django.shortcuts import render
from django.http import HttpResponse

# localhost:8000/gym/.......
def index(request):
    return HttpResponse("Hello, world. You're at the gym index.")
