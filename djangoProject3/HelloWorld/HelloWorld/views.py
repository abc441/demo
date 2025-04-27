from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello World")

def runoob(request):
    context = {}
    context['Hello'] = 'Hello World!'
    return render(request,'runoob.html',context)