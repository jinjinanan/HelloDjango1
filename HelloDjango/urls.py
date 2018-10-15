"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from app1 import views
from AboutModel import views as AbMViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'polls/',include('polls.urls')),
    path(r'index/',views.index),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', AbMViews.articles), # 转发到AboutModel的views的视图
    re_path(r'AboutModel/', include('AboutModel.urls')),# 转发到二级路由
    re_path(r'Practice1/',include('Practice1.urls')),
    re_path(r'captcha',include('captcha.urls'))

]


