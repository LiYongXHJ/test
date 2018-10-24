# coding=utf-8
# @Time    : 2018/10/24 0024 9:02
# @Author  : LiYong
# @Site    : 
# @File    : urls.py


from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index')
]