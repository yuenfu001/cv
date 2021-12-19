from django import http
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def anything(request):
    return HttpResponse("this is the new app for login")