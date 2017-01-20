# -*- coding: utf-8 -*-
"""
Views of learnin_cooking app.

this module handle RESTful API methods.
"""

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import Course, Student, Registration
from .serializers import CourseSerializer, StudentSerializer, \
    RegistrationSerializer, CourseChefDetailSerializer


class CourseViewset(viewsets.ModelViewSet):
    """
    Class that handle restful methods of Courses
    """
    queryset = Course.objects.all().select_related('chef')\
        .prefetch_related('students')
    serializer_class = CourseSerializer

    @list_route()
    def email_view(self, request):
        serializer = CourseChefDetailSerializer(self.queryset, many=True)
        return Response(serializer.data)


class StudentViewset(viewsets.ModelViewSet):
    """
    Class that handle restful methods of Students
    """
    queryset = Student.objects.all().prefetch_related('courses')
    serializer_class = StudentSerializer


class RegistrationViewset(viewsets.ModelViewSet):
    """
    Class that handle restful methods of registrations
    """
    queryset = Registration.objects.all().select_related('course')\
        .select_related('student')
    serializer_class = RegistrationSerializer
