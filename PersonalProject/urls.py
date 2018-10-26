from django.conf.urls import re_path
from django import urls
from . import views

urlpatterns = [
    re_path('^homeMenu/$',views.homeMenu,name='homeMenu')
]