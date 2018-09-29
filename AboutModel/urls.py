from django.conf.urls import re_path
from django.urls import include
from . import views

# app_name = 'AboutModel' #URL names的命名空间

urlpatterns = [
    re_path(r'^report/$',views.report),

#     路由组
    re_path(r'^(?P<page_slug>[0-9]{1})/',include([
        re_path(r'^history/$',views.history),
        re_path(r'^edit/$', views.edit),
    ])),

#     额外参数
    re_path(r'^blog/(?P<year>[0-9]{4})/$',views.year_achive,{'foo':'bar'})
]