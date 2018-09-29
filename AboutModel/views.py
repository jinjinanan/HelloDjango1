from django.shortcuts import render
from django.http import HttpResponse

def articles(request,year):
    return HttpResponse('你好,%s'%year)

def report(request):
    return HttpResponse('你好' )

def history(request,page_slug):
    return HttpResponse('你好,history,%s'%page_slug)

def edit(request):
    return HttpResponse('你好,history')

def year_achive(request,year,foo):
    return HttpResponse('你好, year:%s, foo:%s' % (year,foo))