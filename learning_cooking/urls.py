# -*- coding: utf-8 -*-
"""
URL route tables of learning_cooking app
"""
from django.conf.urls import url
from learning_cooking import views

urlpatterns = [
    url(r'^course/$', views.CourseListCreate.as_view(), ),
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseGetUpdateDelete.as_view()),
    url(r'^registration/$', views.RegistrationListCreate.as_view()),
    url(r'^registration/(?P<pk>[0-9]+)/$',
        views.RegistrationGetUpdateDelete.as_view()),
]
