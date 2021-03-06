# _*_coding:utf-8 _*_
"""
    @Time　　: 2020/3/30   19:27 
    @Author　 : Guoli
    @ File　　  : urls.py
    @Software  : PyCharm
    @Description : 
"""

from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from . import views


urlpatterns = [
    re_path('^$', views.IndexView.as_view()),
    re_path('^(\d+)/$', views.SchoolBase.as_view()),
    re_path('^(\d+)/professional/$', views.ProfessionalView.as_view()),
    re_path('^(\d+)/provinceline/$', views.ProvincelineView.as_view()),
    re_path('^(\d+)/job_area/$', views.Job_area.as_view()),
    re_path('^(\d+)/job_company/$', views.Job_company.as_view()),
    re_path('^(\d+)/comment/$', views.CommentView.as_view()),
    re_path('^search/$', views.SearchView.as_view()),
    re_path('^checkschool/$', views.CheckSchoolname.as_view()),
    re_path('^writecomment/$', views.WriteComment.as_view())
]

