# coding=utf-8
# @Time    : 2018/10/24 0024 9:02
# @Author  : LiYong
# @Site    : 
# @File    : urls.py


from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote")
]