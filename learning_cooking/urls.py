# -*- coding: utf-8 -*-
"""
URL route tables of learning_cooking app
"""
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from learning_cooking import views

router = DefaultRouter()
router.register(r'students', views.StudentViewset)
router.register(r'courses', views.CourseViewset)
router.register(r'registrations', views.RegistrationViewset)

urlpatterns = router.urls

