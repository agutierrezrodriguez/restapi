# -*- coding: utf-8 -*-
"""
Models module for learning cooking django app
"""

from django.db import models
from django_countries.fields import CountryField


class Chef(models.Model):
    """
    Chef model definition
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False,
                              unique=True)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    Student model definition
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=150, null=True)
    zip = models.CharField(max_length=10, null=False, blank=False)
    country = CountryField(null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False,
                              unique=True)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Course model definition
    """
    name = models.CharField(max_length=100, null=False, blank=False,
                            unique=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    chef = models.ForeignKey(Chef)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return self.name


class Registration(models.Model):
    """
    Registration model
    """
    course = models.ForeignKey(Course, null=False, blank=False,
                               related_name='students')
    student = models.ForeignKey(Student, null=False, blank=False,
                                related_name='courses')
    register_date = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u"%s - %s" % (self.course.name, self.student.name)

    def __str__(self):
        return "%s - %s" % (self.course.name, self.student.name)

    class Meta:
        unique_together = (('course', 'student'),)
