# -*- coding: utf-8 -*-
"""
URLs routing for RestAPI Project
"""
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^hc/$', include('health_check.urls')),
    url(r'^', include('learning_cooking.urls')),
]
