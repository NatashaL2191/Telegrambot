from django.shortcuts import render
from re import requests
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")