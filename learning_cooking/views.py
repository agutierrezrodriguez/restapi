# -*- coding: utf-8 -*-
"""
Views of learnin_cooking app.

this module handle RESTful API methods.
"""

from rest_framework import generics, mixins
from .models import Course, Registration
from .serializers import CourseListSerializer, CourseDetailSerializer, \
    RegistrationSerializer


class CourseListCreate(mixins.ListModelMixin, mixins.CreateModelMixin,
                       generics.GenericAPIView):
    """
    Class that handle list and create methods of Courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

    def get(self, request, *args, **kwargs):
        """
        List method of courses
        """
        self.serializer_class = CourseListSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create method of courses
        """
        self.serializer_class = CourseDetailSerializer
        return self.create(request, *args, **kwargs)


class CourseGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Class that handle get, update and delete methods of Courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class RegistrationListCreate(generics.ListCreateAPIView):
    """
    Class that handle list and create methods of Registrations
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Class that handle get, update and delete methods of Registrations
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
