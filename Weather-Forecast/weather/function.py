#coding:utf8
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response


def wea(request):
    return render(request,'wea.html')
