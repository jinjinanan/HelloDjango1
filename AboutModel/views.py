from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def articles(request,year):
    return HttpResponse('你好,%s'%year)

def report(request):
    return HttpResponseRedirect(reverse('blogYear',args=(2014,)))

def history(request,page_slug):
    return HttpResponse('你好,history,%s'%page_slug)

def edit(request,page_slug):
    return render(request,'AboutModel/1.html',{'agram':page_slug})

def year_achive(request,year,foo):
    return HttpResponse('你好, year:%s, foo:%s' % (year,foo))