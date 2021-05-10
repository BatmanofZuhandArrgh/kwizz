from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myView(request):
    print('whoa')
    return HttpResponse('Hello, Thu. I love you. You are my World')
