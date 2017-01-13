# -*- coding: utf-8 -*-
"""
Serializer module of RESTfull API
"""

from rest_framework import serializers
from .models import Course, Registration


class CourseListSerializer(serializers.ModelSerializer):
    """
    List serializer of Course model
    """
    class Meta:
        model = Course
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Detail serializer of Course model
    """
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'start_date', 'end_date',
                  'chef')
        read_only_fields = ('id',)


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer of Registration model
    """
    class Meta:
        model = Registration
        fields = ('id', 'course', 'student', 'register_date')
        read_only_fields = ('id',)
