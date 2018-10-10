from django.conf.urls import re_path
from django.contrib import admin
from Practice1 import views

urlpatterns = [
    re_path(r'index/',views.index),
    re_path(r'login',views.login),
    re_path(r'register/',views.register),
    re_path(r'logout/',views.logout),
]