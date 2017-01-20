# -*- coding: utf-8 -*-
"""
Serializer module of RESTfull API
"""

from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin
from .models import Course, Registration, Student, Chef


class ChefMiniSerializer(serializers.ModelSerializer):
    """
    Serializer of chef email
    """
    class Meta:
        model = Chef
        fields = ('id','email',)
        read_only_fields = ('id',)


class CourseSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    """
    Serializer of Course model
    """
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'start_date', 'end_date',
                  'chef', 'students')
        read_only_fields = ('id', 'students')


class CourseChefDetailSerializer(CourseSerializer):
    """
    Serializer for courses list
    """
    chef = ChefMiniSerializer()


class StudentSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    """
    Serializer of Student model
    """
    class Meta:
        model = Student
        fields = ('id', 'name', 'surname', 'zip', 'country', 'email',
                  'courses')
        read_only_fields = ('id', 'courses')



class RegistrationSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    """
    Serializer of Registration model
    """
    class Meta:
        model = Registration
        fields = ('id', 'course', 'student', 'register_date')
        read_only_fields = ('id',)

